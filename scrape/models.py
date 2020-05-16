from django.db import models


# In order to save to this model manually, use terminal command 'python manage.py savetodb'

class WebScrape(models.Model):
    date = models.CharField(max_length=30)
    counties = models.CharField(max_length=30)
    cases = models.CharField(max_length=30)
    deaths = models.CharField(max_length=30)

    def __str__(self):
        return self.name
