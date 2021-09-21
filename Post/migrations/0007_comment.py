# Generated by Django 3.2.7 on 2021-09-19 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Post', '0006_auto_20210919_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('comment_created_on', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Post.answer')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Post.question')),
            ],
            options={
                'ordering': ['-comment_created_on'],
            },
        ),
    ]
