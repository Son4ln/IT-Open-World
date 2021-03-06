# Generated by Django 2.2.3 on 2019-07-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('avatar', models.ImageField(height_field=500, max_length=500, upload_to=None, verbose_name='Avatar', width_field=500)),
                ('name', models.CharField(max_length=500, unique=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=500, unique=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
