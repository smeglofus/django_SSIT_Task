# Generated by Django 4.1.2 on 2022-12-22 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_timechoice_delete_timechoices'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TimeChoice',
        ),
    ]
