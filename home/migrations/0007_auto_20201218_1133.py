# Generated by Django 3.1.4 on 2020-12-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201218_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='h_image',
            field=models.ImageField(blank=True, default='templates/images/discuss.jpg', height_field='190', null=True, upload_to='', width_field='190'),
        ),
    ]