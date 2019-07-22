# Generated by Django 2.2.3 on 2019-07-22 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20190721_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='myusers',
            name='uid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='userid'),
        ),
    ]
