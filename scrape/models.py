from django.db import models


class WebScrape(models.Model):
    date = models.CharField(max_length=30)
    counties = models.CharField(max_length=30)
    cases = models.CharField(max_length=30)
    deaths = models.CharField(max_length=30)
