# Generated by Django 3.1.4 on 2021-02-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_cart_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cart_key',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
