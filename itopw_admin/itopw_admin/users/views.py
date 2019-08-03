from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class ListUser(TemplateView):
    template_name = 'users/user_list.html'

    def get(self, request, *args, **kwargs):
        """
        Custom query set to filter type of user
        """
        context = self.get_context_data(**kwargs)
        context['total_users'] = User.objects.all().count()
        return self.render_to_response(context)


class UpdateUser(DetailView):
    template_name = 'users/user.html'
    pk_url_kwarg = 'pk'
    queryset = User.objects.all()
