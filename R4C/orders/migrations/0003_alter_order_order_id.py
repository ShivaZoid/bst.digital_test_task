# Generated by Django 4.2.5 on 2023-09-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_id_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
