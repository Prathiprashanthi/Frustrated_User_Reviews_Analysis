# Generated by Django 4.2.4 on 2023-08-22 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0013_user_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
