# Generated by Django 4.0.7 on 2024-10-19 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0005_alertupdate_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alertupdate',
            options={'ordering': ['-modified', '-created']},
        ),
    ]
