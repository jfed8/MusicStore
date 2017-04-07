# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('graphic', models.TextField(blank=True, null=True)),
                ('available', models.BooleanField(default=1)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BulkProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.Product')),
                ('barcode', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('reorder_trigger', models.IntegerField()),
                ('reorder_quantity', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('catalog.product',),
        ),
        migrations.CreateModel(
            name='RentalProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.Product')),
                ('serial_number', models.TextField(blank=True, null=True)),
                ('is_rented', models.BooleanField()),
                ('condition', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('catalog.product',),
        ),
        migrations.CreateModel(
            name='UniqueProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.Product')),
                ('serial_number', models.TextField(blank=True, null=True)),
                ('condition', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('catalog.product',),
        ),
        migrations.AddField(
            model_name='productpicture',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_catalog.product_set+', to='contenttypes.ContentType'),
        ),
    ]
