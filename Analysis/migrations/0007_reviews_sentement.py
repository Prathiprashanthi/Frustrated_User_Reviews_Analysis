# Generated by Django 4.2.4 on 2023-08-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0006_alter_user_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='Sentement',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
