from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.generic import UpdateView, DetailView, TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import UserProfile
from checkout.models import Product
from .forms import UserProfileForm
from checkout.models import Order

class AdminOrSuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

class ProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return get_object_or_404(UserProfile, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context['form'] = self.form_class(instance=profile)
        context['orders'] = profile.orders.order_by('-date') if hasattr(profile, 'orders') else []
        context['on_profile_page'] = True
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Profile updated successfully')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        messages.error(self.request, 'Please correct the error below.')
        return self.render_to_response(context)


class OrderHistoryView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'checkout_success.html'
    context_object_name = 'order'

    def get_object(self):
        order_number = self.kwargs.get('order_number')
        return get_object_or_404(Order, order_number=order_number)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.info(self.request, (
            f'This is a past confirmation for order number {self.object.order_number}. '
            'A confirmation email was sent on the order date.'
        ))
        context['from_profile'] = True
        return context


class SiteManagementView(LoginRequiredMixin, AdminOrSuperuserRequiredMixin, TemplateView):
    template_name = 'site_management/site_management.html'
