from django.db import models

# Create your models here.
class Blog(models.Model):
    b_heading = models.TextField(default='default heading...')
    b_paragraphs = models.TextField(default='default content...')

