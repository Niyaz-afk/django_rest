# Generated by Django 3.1.2 on 2020-10-31 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_auto_20201031_0909'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Public',
            new_name='Post',
        ),
    ]