from django.db import models

# Create your models here.

class Contact(models.Model):
    c_heading = models.TextField(default='default heading...')
    c_paragraphs = models.TextField(default='default content...')
