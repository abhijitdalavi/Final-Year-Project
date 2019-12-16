# Generated by Django 2.1.5 on 2019-03-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=500, null=True)),
                ('product_url', models.CharField(blank=True, max_length=500, null=True)),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('product_image', models.CharField(blank=True, max_length=400, null=True)),
                ('vendor_name', models.CharField(blank=True, max_length=20, null=True)),
                ('product_category', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]