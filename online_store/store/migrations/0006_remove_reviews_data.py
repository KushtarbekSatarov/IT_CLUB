# Generated by Django 5.0.4 on 2024-05-06 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_reviews_reviews_reviews_descriptions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='data',
        ),
    ]
