# Generated by Django 2.2 on 2019-06-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20190603_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nick_name',
            field=models.CharField(blank='False', max_length=50, null='False'),
        ),
    ]
