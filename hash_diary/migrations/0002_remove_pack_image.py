# Generated by Django 2.1.2 on 2018-10-08 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hash_diary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pack',
            name='image',
        ),
    ]
