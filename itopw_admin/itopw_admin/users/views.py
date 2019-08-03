from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, TemplateView, FormView
from django.shortcuts import get_object_or_404

from itopw_admin.users.forms import SuperUpdateUserForm

User = get_user_model()


class ListUser(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_list.html'

    def get(self, request, *args, **kwargs):
        """
        Custom query set to filter type of user
        """
        context = self.get_context_data(**kwargs)
        context['total_users'] = User.objects.all().count()
        return self.render_to_response(context)


class UpdateUser(LoginRequiredMixin, FormView):
    template_name = 'users/user.html'
    form_class = SuperUpdateUserForm

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        context = self.get_context_data()
        context['object'] = get_object_or_404(User, pk=kwargs['pk'])
        return self.render_to_response(context)

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**self.get_form_kwargs())
