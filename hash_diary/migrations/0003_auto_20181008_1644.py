# Generated by Django 2.1.2 on 2018-10-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hash_diary', '0002_remove_pack_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='short_name',
            field=models.CharField(default='Misc H3', max_length=20, verbose_name='Short name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pack',
            name='name',
            field=models.CharField(default='Your name H3', max_length=200, verbose_name='Name'),
        ),
    ]
