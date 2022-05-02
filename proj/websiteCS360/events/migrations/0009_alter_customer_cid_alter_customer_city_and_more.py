# Generated by Django 4.0.4 on 2022-05-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_alter_customer_cid_alter_customer_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CID',
            field=models.IntegerField(max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='customer',
            name='firstName',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lastName',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipCode',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='PID',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.TextField(max_length=60),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='CID',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='PID',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='VID',
            field=models.IntegerField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='companyName',
            field=models.TextField(max_length=120),
        ),
    ]