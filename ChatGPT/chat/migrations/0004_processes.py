# Generated by Django 4.2.1 on 2023-05-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_hotel_img_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img_url', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]