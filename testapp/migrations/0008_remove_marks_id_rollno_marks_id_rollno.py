# Generated by Django 4.1.7 on 2023-02-21 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_alter_marks_id_rollno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marks',
            name='id_rollno',
        ),
        migrations.AddField(
            model_name='marks',
            name='id_rollno',
            field=models.ManyToManyField(to='testapp.student'),
        ),
    ]
