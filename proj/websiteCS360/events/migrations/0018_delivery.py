# Generated by Django 4.0.4 on 2022-05-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_alter_product_brand_alter_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('DID', models.IntegerField(primary_key=True, serialize=False)),
                ('shippingCost', models.TextField(max_length=100)),
                ('shippingTime', models.TextField(max_length=100)),
            ],
        ),
    ]
