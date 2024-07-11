# Generated by Django 5.0.4 on 2024-07-11 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_processeddata_top_selling_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processeddata',
            name='daily_total_sales',
        ),
        migrations.RemoveField(
            model_name='processeddata',
            name='total_sales_by_product',
        ),
        migrations.AddField(
            model_name='processeddata',
            name='total_sales',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='processeddata',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='processeddata',
            name='store_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='processeddata',
            name='top_selling_product',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
