# Generated by Django 2.1 on 2018-08-06 23:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0007_auto_20180802_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 6, 23, 14, 26, 211399, tzinfo=utc)),
        ),
    ]
