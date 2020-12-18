from django.db import models

# Create your models here.
class Service(models.Model):
    s_heading = models.TextField(default='default heading...')
    s_paragraphs = models.TextField(default='default content...')
