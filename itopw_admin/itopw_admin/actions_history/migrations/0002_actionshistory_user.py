# Generated by Django 2.2.3 on 2019-07-03 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actions_history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionshistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions_history', to=settings.AUTH_USER_MODEL),
        ),
    ]
