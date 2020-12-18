from django.db import models

# Create your models here.
class About(models.Model):
    a_heading = models.TextField(default='default heading...')
    a_paragraphs = models.TextField(default='default content...')
