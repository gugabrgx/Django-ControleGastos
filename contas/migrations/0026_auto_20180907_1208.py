# Generated by Django 2.1 on 2018-09-07 15:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0025_auto_20180906_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 7, 15, 8, 39, 557551, tzinfo=utc)),
        ),
    ]
