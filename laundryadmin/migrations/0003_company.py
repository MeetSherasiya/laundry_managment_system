# Generated by Django 4.2.3 on 2023-08-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundryadmin', '0002_alter_price_bottomwear_alter_price_topwear_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comapny_name', models.CharField(max_length=100)),
                ('comapny_email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
            ],
        ),
    ]
