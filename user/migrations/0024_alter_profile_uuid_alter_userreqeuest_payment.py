# Generated by Django 4.2.3 on 2023-07-31 17:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_userreqeuest_payment_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0b6fd435-7992-4ffe-8e01-e2a9fe7ffc6c'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userreqeuest',
            name='payment',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Cash', 'Cash'), ('Online', 'Online')], max_length=10),
        ),
    ]
