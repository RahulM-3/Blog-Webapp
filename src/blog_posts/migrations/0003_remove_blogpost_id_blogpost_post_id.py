# Generated by Django 5.0.4 on 2024-04-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0002_blogpost_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='id',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
