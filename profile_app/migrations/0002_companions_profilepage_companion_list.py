# Generated by Django 4.0.7 on 2024-10-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('relationship_type', models.CharField(choices=[('select option', 'Select Option'), ('spouse', 'Spouse'), ('parent', 'Parent'), ('child', 'Child'), ('sibling', 'Sibling'), ('friend', 'Friend'), ('in-law', 'In-Law'), ('neighbor', 'Neighbor'), ('non-related', 'Non-Related')], default='select option', max_length=25)),
                ('profile_photo', models.ImageField(upload_to='profile_photos/')),
            ],
        ),
        migrations.AddField(
            model_name='profilepage',
            name='companion_list',
            field=models.ManyToManyField(related_name='profile_companions', to='profile_app.companions'),
        ),
    ]
