from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from .forms import ContactMessageForm


class HomeView(TemplateView):
    template_name = "pages/home.html"


class ServicesWebDevelopmentView(TemplateView):
    template_name = "pages/services_web_development.html"


class ServicesSeoView(TemplateView):
    template_name = "pages/services_seo.html"


class PortfolioView(TemplateView):
    template_name = "pages/portfolio.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ContactView(CreateView):
    template_name = "pages/contact.html"
    form_class = ContactMessageForm
    success_url = reverse_lazy('contact')
