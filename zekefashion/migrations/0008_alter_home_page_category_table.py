# Generated by Django 4.0 on 2021-12-31 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zekefashion', '0007_alter_home_page_category_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='home_page_category',
            table='category',
        ),
    ]
