# Generated by Django 4.0.7 on 2024-10-19 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0009_alter_companion_relationship_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companion',
            name='relationship_type',
            field=models.CharField(max_length=30),
        ),
    ]
