from django.contrib.sitemaps.views import sitemap
from django.urls import path

from .sitemaps import StaticViewSitemap
from . import views

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("services-web-development/", views.ServicesWebDevelopmentView.as_view(), name="services-web-development"),
    path("services-seo/", views.ServicesSeoView.as_view(), name="services-seo"),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path("about/", views.AboutView.as_view(), name="about"),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django-sitemap",),
]
