# Generated by Django 2.2.3 on 2019-07-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, max_length=500, null=True, upload_to=None, verbose_name='File Url')),
                ('name', models.CharField(max_length=500, unique=True, verbose_name='Title')),
                ('size', models.IntegerField(default=0, verbose_name='File Size')),
                ('mime', models.CharField(max_length=10, verbose_name='File Mime')),
            ],
        ),
    ]
