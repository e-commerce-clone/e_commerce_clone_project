# Generated by Django 3.1.4 on 2021-02-22 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cart_key',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
