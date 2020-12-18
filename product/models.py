from django.db import models

# Create your models here.
class Product(models.Model):
    p_heading = models.TextField(default='default heading...')
    p_paragraphs = models.TextField(default='default content...')
