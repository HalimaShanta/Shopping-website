# Generated by Django 3.0.8 on 2021-08-16 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_customer_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cutomer',
            new_name='customer',
        ),
    ]