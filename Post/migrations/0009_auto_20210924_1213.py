# Generated by Django 3.2.7 on 2021-09-24 06:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0008_auto_20210924_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Views',
            field=models.ManyToManyField(blank=True, null=True, related_name='Qviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='Upvotes_Que',
            field=models.ManyToManyField(blank=True, null=True, related_name='Qupvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
