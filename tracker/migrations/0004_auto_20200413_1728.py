 # Generated by Django 3.0.5 on 2020-04-13 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_customer_order_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Issues',
        ),
    ]
