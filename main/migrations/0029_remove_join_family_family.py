# Generated by Django 4.0.5 on 2022-11-23 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_join_team_join_family'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join_family',
            name='Family',
        ),
    ]
