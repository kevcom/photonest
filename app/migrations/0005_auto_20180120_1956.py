# Generated by Django 2.0.1 on 2018-01-20 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_image_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='last_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]