# Generated by Django 4.1.2 on 2022-12-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_timechoice_time_alter_timechoice_vote_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='timechoice',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timechoice',
            name='time',
            field=models.CharField(max_length=15),
        ),
    ]
