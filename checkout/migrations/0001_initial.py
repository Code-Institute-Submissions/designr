# Generated by Django 3.1.6 on 2021-02-27 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_auto_20210221_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=40)),
                ('postcode', models.CharField(max_length=20)),
                ('town_or_city', models.CharField(max_length=40)),
                ('street_address1', models.CharField(max_length=80)),
                ('street_address2', models.CharField(max_length=80)),
                ('county', models.CharField(max_length=80)),
                ('date', models.DateTimeField(auto_now=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
        ),
    ]
