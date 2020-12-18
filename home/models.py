from django.db import models

# Create your models here.
class Home(models.Model):
    h_heading    = models.TextField(default='default heading...')
    h_paragraphs = models.TextField(default='default content...')
    h_image      = models.ImageField(blank=False,null=False,default='templates/images/discuss.jpg',editable=True,width_field='image_height',height_field='image_width')
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="190")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="190")
