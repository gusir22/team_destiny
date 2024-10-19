# Generated by Django 4.0.7 on 2024-10-19 02:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evacuation_status', models.CharField(choices=[('evacuated', 'Evacuated'), ('non_evacuated', 'Non-Evacuated')], default='non_evacuated', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_page', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
