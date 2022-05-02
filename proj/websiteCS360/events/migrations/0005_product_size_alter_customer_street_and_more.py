# Generated by Django 4.0.4 on 2022-05-01 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_merge_0003_delete_ingressflow_0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default=2, max_length=60, verbose_name='Product Size'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.CharField(max_length=300, verbose_name='Street'),
        ),
        migrations.DeleteModel(
            name='Requirement',
        ),
    ]
