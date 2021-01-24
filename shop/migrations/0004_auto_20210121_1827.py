# Generated by Django 3.1.4 on 2021-01-21 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('shop', '0003_auto_20210116_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='main_image',
            field=models.ImageField(upload_to='products/mainImage/%Y/%m/%d', verbose_name='메인 이미지'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='sub_image',
            field=models.ImageField(upload_to='products/subImage/%Y/%m/%d', verbose_name='서브 이미지'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('image', models.ImageField(upload_to='products/reviewImage/%Y/%m/%d', verbose_name='후기 이미지')),
                ('text', models.TextField(verbose_name='내용')),
                ('help', models.PositiveIntegerField(default=0, null=True, verbose_name='도움')),
                ('lookup', models.PositiveIntegerField(default=0, null=True, verbose_name='조회')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='작성일')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profile')),
            ],
        ),
    ]