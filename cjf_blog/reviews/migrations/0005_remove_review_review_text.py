# Generated by Django 2.0.3 on 2018-05-05 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_review_markdown'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_text',
        ),
    ]