# Generated by Django 4.2.7 on 2023-11-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_code', models.CharField(max_length=20, unique=True)),
                ('supplier_name', models.CharField(max_length=255)),
                ('supplier_address', models.TextField()),
                ('supplier_city', models.CharField(max_length=50)),
                ('supplier_country', models.CharField(max_length=50)),
                ('supplier_postalCode', models.CharField(max_length=10)),
                ('supplier_addedDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]