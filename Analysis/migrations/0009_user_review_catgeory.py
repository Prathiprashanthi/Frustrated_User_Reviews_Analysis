# Generated by Django 4.2.4 on 2023-08-17 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0008_remove_reviews_sentement_reviews_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Review_Catgeory',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
