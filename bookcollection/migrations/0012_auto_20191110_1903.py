# Generated by Django 2.2.1 on 2019-11-10 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0011_auto_20191110_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstances',
            options={'ordering': ['id'], 'permissions': (('can_mark_returned', 'set book as returned '), ('staff', 'for staff only'))},
        ),
    ]