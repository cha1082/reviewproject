# Generated by Django 3.2.4 on 2021-07-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewpost', '0003_rename_useful_review_record_reviewmodel_fastest_delivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingMediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
                ('shopping_cart', models.ImageField(upload_to='')),
            ],
        ),
    ]
