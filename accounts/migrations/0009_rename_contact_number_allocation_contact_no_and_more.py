# Generated by Django 5.1.5 on 2025-02-17 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_allocation_adapter_allocation_asset_tag_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allocation',
            old_name='contact_number',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='others_category',
            new_name='other_assets',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='request_number',
            new_name='request_no',
        ),
        migrations.RenameField(
            model_name='allocation',
            old_name='seat_number',
            new_name='seat_no',
        ),
    ]
