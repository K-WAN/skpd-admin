# Generated by Django 2.1.5 on 2019-02-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20190115_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='atm',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='atm',
            name='atm_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
