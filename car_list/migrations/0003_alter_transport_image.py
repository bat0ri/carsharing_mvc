# Generated by Django 4.1.7 on 2023-05-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_list', '0002_transport_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='image',
            field=models.ImageField(upload_to='transport_images/'),
        ),
    ]
