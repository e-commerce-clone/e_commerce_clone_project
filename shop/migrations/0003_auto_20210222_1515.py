# Generated by Django 3.1.4 on 2021-02-22 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210207_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['main_category'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='meta_description',
            field=models.TextField(blank=True, default=''),
        ),
    ]