# Generated by Django 3.2.11 on 2022-02-28 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='expected_delivert_date',
            new_name='expected_delivery_date',
        ),
    ]