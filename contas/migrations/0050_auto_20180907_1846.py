# Generated by Django 2.1 on 2018-09-07 21:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0049_auto_20180907_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 7, 21, 46, 48, 607262, tzinfo=utc)),
        ),
    ]
