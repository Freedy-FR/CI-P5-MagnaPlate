"""
Views for the checkout process, including checkout page, checkout success
page, and cache checkout data.
"""

import json
import stripe

from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from cart.contexts import cart_contents


class CacheCheckoutDataView(View):
    """
    View to cache checkout data for stripe payments.
    """
    def post(self, request, *args, **kwargs):
        try:
            pid = request.POST.get('client_secret').split('_secret')[0]
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.PaymentIntent.modify(pid, metadata={
                'cart': json.dumps(request.session.get('cart', {})),
                'save_info': request.POST.get('save_info'),
                'username': request.user,
            })
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(
                request,
                'Sorry, your payment cannot be processed right now. '
                'Please try again later.'
            )
            return HttpResponse(content=str(e), status=400)


class CheckoutView(View):
    """
    View to handle the checkout process.
    """
    def get(self, request, *args, **kwargs):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request,
                "There's nothing in your cart at the moment"
            )
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Prefill the form with user profile data if authenticated
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_contact_full_name,
                    'email': profile.default_contact_email,
                    'delivery_phone_number': (
                        profile.default_delivery_phone_number
                    ),
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(
                request,
                'Stripe public key is missing. '
                'Did you forget to set it in your environment?'
            )

        template = 'checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'delivery_phone_number': request.POST['delivery_phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            if request.user.is_authenticated:
                order.user_profile = get_object_or_404(
                    UserProfile, user=request.user
                )
            order.save()

            for item_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your cart wasn't found in our "
                        "database. Please call us for assistance!"
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            # Save the info to the user's profile if all is well
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )
        else:
            messages.error(
                request,
                'There was an error with your form. '
                'Please double check your information.'
            )

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if not stripe_public_key:
            messages.warning(
                request,
                'Stripe public key is missing. '
                'Did you forget to set it in your environment?'
            )

        template = 'checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


class CheckoutSuccessView(DetailView):
    """
    View to handle successful checkouts.
    """
    model = Order
    template_name = 'checkout_success.html'
    context_object_name = 'order'

    def get_object(self):
        order_number = self.kwargs.get('order_number')
        return get_object_or_404(Order, order_number=order_number)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        save_info = self.request.session.get('save_info')

        # Attach the user's profile to the order if authenticated
        if self.request.user.is_authenticated:
            profile = get_object_or_404(UserProfile, user=self.request.user)
            order.user_profile = profile
            order.save()

            # Save the user's info if save_info is true
            if save_info:
                profile_data = {
                    'default_contact_full_name': (
                        profile.default_contact_full_name
                    ),
                    'default_contact_email': profile.default_contact_email,
                    'default_contact_phone_number': (
                        profile.default_contact_phone_number
                    ),
                    'default_delivery_phone_number': (
                        order.delivery_phone_number
                    ),
                    'default_country': order.country,
                    'default_postcode': order.postcode,
                    'default_town_or_city': order.town_or_city,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                    'default_county': order.county,
                }
                user_profile_form = UserProfileForm(
                    profile_data, instance=profile
                )
                if user_profile_form.is_valid():
                    user_profile_form.save()

        # Custom context
        context['order'] = order

        messages.success(
            self.request,
            f'Order successfully processed! Your order number is '
            f'{order.order_number}. A confirmation email will be sent '
            f'to {order.email}.'
        )

        if 'cart' in self.request.session:
            del self.request.session['cart']

        return context
