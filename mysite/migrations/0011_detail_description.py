# Generated by Django 2.2.24 on 2021-06-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_detail_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='description',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
