# Generated by Django 5.0.12 on 2025-02-14 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_allocation_adapter_allocation_asset_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocation',
            name='bag',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='confirmed',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='mouse',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='project_specific',
        ),
        migrations.RemoveField(
            model_name='allocation',
            name='short_term',
        ),
    ]
