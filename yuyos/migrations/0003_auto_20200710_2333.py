# Generated by Django 3.0.7 on 2020-07-11 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuyos', '0002_auto_20200707_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente_moroso',
            name='rut_cliente_moroso',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
