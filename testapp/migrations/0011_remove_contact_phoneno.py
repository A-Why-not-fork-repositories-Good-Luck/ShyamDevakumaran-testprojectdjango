# Generated by Django 4.1.7 on 2023-02-27 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phoneno',
        ),
    ]