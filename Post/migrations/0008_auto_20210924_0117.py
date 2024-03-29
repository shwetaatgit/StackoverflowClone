# Generated by Django 3.2.7 on 2021-09-23 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Upvotes_Que',
            field=models.ManyToManyField(blank=True, null=True, related_name='Upvotes_Que', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments_ans', to='Post.answer'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Post.question'),
        ),
    ]
