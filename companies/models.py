from django.db import models

class Companies(models.Model):
	company_id = models.IntegerField(blank=False)
	ticker = models.CharField(max_length=10, blank=True)
	company_full_name = models.CharField(max_length=100)
	company_short_name = models.CharField(max_length=50)
	official_site = models.URLField(blank=True)
	ceo = models.CharField(max_length=50, blank=True)
	industry = models.CharField(max_length=50, blank=True)
	company_description = models.TextField()