# Generated by Django 3.2.4 on 2021-07-06 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0006_shoppingcartmodel_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcartmodel',
            name='item',
        ),
    ]