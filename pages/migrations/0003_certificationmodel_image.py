# Generated by Django 4.2.6 on 2023-10-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_certificationmodel_whoarewemodel_bannermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificationmodel',
            name='image',
            field=models.ImageField(default='default_image.png', upload_to='certifications/'),
        ),
    ]
