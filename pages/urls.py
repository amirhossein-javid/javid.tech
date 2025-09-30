from django.urls import path

from .views import HomeView, ServicesWebDevelopmentView, ServicesSeoView, PortfolioView, AboutView, ContactView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("services-web-development/", ServicesWebDevelopmentView.as_view(), name="services-web-development"),
    path("services-seo/", ServicesSeoView.as_view(), name="services-seo"),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    path("about/", AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name='contact'),
]
