# Generated by Django 2.2.3 on 2019-08-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190803_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_writter',
            field=models.BooleanField(default=False, verbose_name='Writter'),
        ),
    ]
