# Generated by Django 2.2.3 on 2019-07-21 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_myusers_wish'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myusers',
            old_name='name',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='myusers',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='myusers',
            name='wish',
        ),
    ]
