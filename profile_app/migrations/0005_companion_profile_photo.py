# Generated by Django 4.0.7 on 2024-10-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0004_alter_companion_relationship_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='companion',
            name='profile_photo',
            field=models.ImageField(default='now', upload_to='profile_photos/'),
            preserve_default=False,
        ),
    ]
