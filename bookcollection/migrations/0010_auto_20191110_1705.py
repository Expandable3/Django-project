# Generated by Django 2.2.1 on 2019-11-10 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookcollection', '0009_auto_20191110_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstances',
            options={'ordering': ['id'], 'permissions': (('can_mark_returned', 'set book as returned '),)},
        ),
    ]