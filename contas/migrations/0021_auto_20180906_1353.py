# Generated by Django 2.1.1 on 2018-09-06 16:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0020_auto_20180906_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 6, 16, 53, 2, 129933, tzinfo=utc)),
        ),
    ]