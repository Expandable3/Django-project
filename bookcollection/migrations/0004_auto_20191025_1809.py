# Generated by Django 2.2.1 on 2019-10-25 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0003_auto_20191025_1806'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
    ]