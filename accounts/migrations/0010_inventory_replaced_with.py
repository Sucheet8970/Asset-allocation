# Generated by Django 5.1.5 on 2025-02-06 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_laptop_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='replaced_with',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replaced_asset', to='accounts.inventory'),
        ),
    ]
