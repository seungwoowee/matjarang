# Generated by Django 2.2 on 2020-10-04 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HoobangList', '0003_hoobanglist_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hoobanglist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
