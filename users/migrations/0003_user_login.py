# Generated by Django 4.1.5 on 2023-01-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(default='', max_length=150, verbose_name='логин'),
            preserve_default=False,
        ),
    ]
