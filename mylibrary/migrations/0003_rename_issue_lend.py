# Generated by Django 4.0.8 on 2022-10-09 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylibrary', '0002_person_issue'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Issue',
            new_name='Lend',
        ),
    ]