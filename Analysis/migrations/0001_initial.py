# Generated by Django 4.2.4 on 2023-08-11 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('UserFullname', models.CharField(max_length=50)),
                ('UserEmail', models.EmailField(max_length=50)),
                ('UserPassword', models.TextField(max_length=10)),
                ('UserContact', models.TextField(max_length=10)),
                ('UserImage', models.FileField(null=True, upload_to='media')),
            ],
        ),
    ]