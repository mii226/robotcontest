# Generated by Django 2.1.5 on 2019-02-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robot', '0004_auto_20190215_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
