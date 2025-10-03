from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return ["home", "services-web-development", "services-seo", "portfolio", "about", "contact"]

    def location(self, item):
        return reverse(item)
    