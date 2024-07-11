# Generated by Django 5.0.4 on 2024-07-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_remove_processeddata_total_sales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processeddata',
            name='daily_total_sales',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='processeddata',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processeddata',
            name='total_sales_by_product',
            field=models.FloatField(blank=True, null=True),
        ),
    ]