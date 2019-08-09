# Generated by Django 2.2.3 on 2019-08-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_is_deactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_notification',
            field=models.BooleanField(default=False, verbose_name='Email Notification'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='user',
            name='web_notification',
            field=models.BooleanField(default=False, verbose_name='Website Notification'),
        ),
    ]