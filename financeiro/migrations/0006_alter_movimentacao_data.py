# Generated by Django 4.1.1 on 2022-09-09 12:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0005_poupanca_alter_movimentacao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacao',
            name='data',
            field=models.DateField(default=datetime.datetime(2022, 9, 9, 12, 26, 57, 207509, tzinfo=datetime.timezone.utc), verbose_name='Data'),
        ),
    ]