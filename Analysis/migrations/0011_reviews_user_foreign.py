# Generated by Django 4.2.4 on 2023-08-18 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0010_reviews_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='User_Foreign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Analysis.user'),
        ),
    ]
