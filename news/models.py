from django.db import models
from django.utils import timezone

class NewsFeed(models.Model):
    company_id = models.CharField(max_length=6)
    added_at = models.DateTimeField(default=timezone.now)
    news_short = models.TextField(blank=True)
    news_url = models.URLField(unique=True)