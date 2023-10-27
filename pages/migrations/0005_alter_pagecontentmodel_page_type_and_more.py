# Generated by Django 4.2.6 on 2023-10-26 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0004_remove_bannermodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontentmodel',
            name='page_type',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page_content', to='pages.pagetypemodel', verbose_name='Page Content'),
        ),
        migrations.AlterField(
            model_name='pagecontentmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_contents', related_query_name='page_contents_user_field', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='pagecontentmodel',
            table='page_content',
        ),
    ]
