from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashBoard(LoginRequiredMixin, TemplateView):
    template_name = 'pages/home.html'
