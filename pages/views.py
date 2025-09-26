from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"


class ServicesWebDevelopmentView(TemplateView):
    template_name = "pages/services_web_development.html"
