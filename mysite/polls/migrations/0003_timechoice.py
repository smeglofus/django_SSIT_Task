# Generated by Django 4.1.2 on 2022-12-20 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_vote_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=5)),
                ('vote_count', models.PositiveIntegerField(default=0)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.choice')),
            ],
        ),
    ]
