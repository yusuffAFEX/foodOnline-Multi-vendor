# Generated by Django 4.1 on 2022-12-19 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_total_data_order_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tax_data',
            field=models.JSONField(blank=True, help_text="Data format: {'tax_type': {'tax_percentage': 'tax_amount'}}", null=True),
        ),
    ]
