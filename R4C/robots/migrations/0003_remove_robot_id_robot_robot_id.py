# Generated by Django 4.2.5 on 2023-09-26 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0002_alter_robot_model_alter_robot_serial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='id',
        ),
        migrations.AddField(
            model_name='robot',
            name='robot_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
