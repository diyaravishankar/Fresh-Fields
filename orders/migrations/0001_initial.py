# Generated by Django 5.0.3 on 2024-04-21 20:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('coupons', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(blank=True, max_length=32, null=True)),
                ('order_id', models.CharField(blank=True, max_length=7, null=True)),
                ('order_status', models.IntegerField(choices=[(1, 'New'), (2, 'Processing'), (3, 'Ready to ship'), (4, 'Shipped'), (5, 'Delivered'), (6, 'Canceled')], default=1, verbose_name='Order status')),
                ('total_amount', models.IntegerField(default=0, verbose_name='Total amount of order')),
                ('payment_method', models.IntegerField(choices=[(1, 'By cash'), (2, 'By card'), (3, 'By balance'), (4, 'By Paypal')], default=1, verbose_name='Payment method')),
                ('activate_balance', models.BooleanField(default=False, verbose_name='Activate Balance')),
                ('comment', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Comment')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupons.usercoupons', verbose_name='Coupon')),
                ('shipping_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.usershippinginfo', verbose_name='User shipping info')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['total_amount'],
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('total_price', models.IntegerField(default=0, verbose_name='Total price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='accounts.store', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'Items in order',
                'ordering': ['total_price'],
            },
        ),
    ]
