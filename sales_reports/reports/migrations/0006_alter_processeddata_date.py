# Generated by Django 5.0.4 on 2024-07-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_remove_processeddata_daily_total_sales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processeddata',
            name='date',
            field=models.DateField(),
        ),
    ]