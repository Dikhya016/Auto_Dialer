# Generated by Django 5.0.6 on 2024-05-19 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_callrecords_call_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='callrecords',
            name='call_result',
            field=models.CharField(default='Unanswered', max_length=30),
        ),
        migrations.AlterField(
            model_name='callrecords',
            name='call_timestamp',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 5, 20, 5, 47, 55, 323509)),
        ),
    ]