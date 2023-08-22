# Generated by Django 4.2.4 on 2023-08-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0004_user_otp_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('ReviewId', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=50)),
                ('Userreview', models.TextField(max_length=200)),
                ('Rating', models.IntegerField()),
                ('catgory', models.TextField(max_length=20)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_reviews',
            },
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
