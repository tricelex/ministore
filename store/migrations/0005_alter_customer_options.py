# Generated by Django 4.0.5 on 2022-08-07 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_order_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={
                'ordering': ['user__first_name', 'user__last_name'],
                'permissions': [('view_history', 'Can view history')],
            },
        ),
    ]
