# Generated by Django 4.1.5 on 2023-03-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0004_alter_tax_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax',
            name='price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Стоимость'),
        ),
    ]