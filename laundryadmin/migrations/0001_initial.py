# Generated by Django 4.2.3 on 2023-07-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topwear', models.IntegerField(max_length=5)),
                ('bottomwear', models.IntegerField(max_length=5)),
                ('woolenwear', models.IntegerField(max_length=5)),
            ],
        ),
    ]
