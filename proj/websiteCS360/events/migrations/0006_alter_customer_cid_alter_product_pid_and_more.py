

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_product_size_alter_customer_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='CID',
            field=models.CharField(max_length=500, verbose_name='CID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PID',
            field=models.CharField(max_length=1000, verbose_name='Product ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=1000, verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='VID',
            field=models.CharField(max_length=1000, verbose_name='VID'),
        ),
    ]
