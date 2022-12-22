# Generated by Django 4.1.2 on 2022-12-22 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_rename_timechoice_timechoices'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.CharField(max_length=15)),
                ('vote_count', models.PositiveIntegerField(default=0)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.choice')),
            ],
        ),
        migrations.DeleteModel(
            name='TimeChoices',
        ),
    ]
