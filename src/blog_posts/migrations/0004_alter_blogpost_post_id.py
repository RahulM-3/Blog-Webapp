# Generated by Django 5.0.4 on 2024-04-19 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0003_remove_blogpost_id_blogpost_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]