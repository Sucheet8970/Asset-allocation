# Generated by Django 5.1.5 on 2025-02-17 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_allocation_bag_remove_allocation_confirmed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='adapter',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='asset_category',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='asset_tag_number',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='battery_sl',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='building',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='department',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='hard_disk',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='manager',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='model',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='other_description',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='processor',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='ram_size',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='request_number',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='seat_number',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='serial_number',
        ),
        migrations.AddField(
            model_name='allocation',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
