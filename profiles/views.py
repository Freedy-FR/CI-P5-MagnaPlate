from django.views.generic import TemplateView

class ProfileView(TemplateView):
    """ Display the user's profile. """
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any context data you need here
        return context
