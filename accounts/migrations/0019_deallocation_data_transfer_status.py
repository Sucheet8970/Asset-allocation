# Generated by Django 5.1.5 on 2025-02-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_deallocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='deallocation',
            name='data_transfer_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
