# Generated by Django 2.0.3 on 2018-05-05 19:46

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20180418_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_markdown',
            field=markdownx.models.MarkdownxField(default='Post not written yet...'),
        ),
    ]