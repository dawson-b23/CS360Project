# Generated by Django 4.0.4 on 2022-05-05 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_remove_customer_id_remove_delivery_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]