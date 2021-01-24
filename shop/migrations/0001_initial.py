# Generated by Django 3.1.4 on 2021-01-12 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('meta_description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, null=True, verbose_name='제품명')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/%Y/%m/%d', verbose_name='이미지')),
                ('sales_unit', models.CharField(max_length=10, null=True, verbose_name='판매단위')),
                ('weight', models.CharField(max_length=10, null=True, verbose_name='중량/용량')),
                ('delivery', models.CharField(max_length=200, null=True, verbose_name='배송구분')),
                ('description', models.TextField(blank=True, verbose_name='설명')),
                ('origin', models.CharField(max_length=50, null=True, verbose_name='원산지')),
                ('packing_type', models.CharField(max_length=50, null=True, verbose_name='포장타입')),
                ('allergy', models.CharField(max_length=200, null=True, verbose_name='알레르기정보')),
                ('shelf_life', models.CharField(max_length=200, null=True, verbose_name='유통기한')),
                ('meta_description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='가격')),
                ('stock', models.PositiveIntegerField(null=True, verbose_name='재고')),
                ('available_display', models.BooleanField(default=True, verbose_name='판매가능여부')),
                ('available_order', models.BooleanField(default=True, verbose_name='주문가능여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='갱신 시간')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.category')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
    ]