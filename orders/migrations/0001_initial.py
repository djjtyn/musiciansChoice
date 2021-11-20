# Generated by Django 2.1.15 on 2021-11-20 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instruments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='purchased')),
                ('totalCost', models.FloatField()),
                ('delivery_street', models.CharField(max_length=80)),
                ('delivery_town', models.CharField(max_length=28)),
                ('delivery_county', models.CharField(max_length=14)),
                ('delivery_postcode', models.CharField(max_length=9)),
                ('customer_phone', models.CharField(max_length=30)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='instruments.Instrument')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.Order')),
            ],
        ),
    ]
