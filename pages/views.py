from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"


class ServicesWebDevelopmentView(TemplateView):
    template_name = "pages/services_web_development.html"


class ServicesSeoView(TemplateView):
    template_name = "pages/services_seo.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"
    