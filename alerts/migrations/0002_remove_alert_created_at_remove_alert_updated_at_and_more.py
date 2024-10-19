# Generated by Django 4.0.7 on 2024-10-19 06:07

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='alert',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='alert',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
