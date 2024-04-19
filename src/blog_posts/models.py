from django.db import models

# Create your models here.

class BlogPost(models.Model):
    post_id = models.IntegerField(primary_key=True)
    title = models.TextField()
    content = models.TextField(null=True, blank=True)