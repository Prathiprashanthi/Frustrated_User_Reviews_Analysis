# Generated by Django 4.2.4 on 2023-08-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0012_user_ratings_user_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
