# Generated by Django 4.0.5 on 2022-11-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_week_message_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.IntegerField()),
                ('Purpose', models.CharField(max_length=200)),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
