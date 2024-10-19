# Generated by Django 4.0.7 on 2024-10-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0008_alter_companion_relationship_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companion',
            name='relationship_type',
            field=models.CharField(choices=[('select_option', 'Select Option'), ('spouse', 'Spouse'), ('parent', 'Parent'), ('child', 'Child'), ('sibling', 'Sibling'), ('in-law', 'In-Law'), ('friend', 'Friend'), ('neighbor', 'Neighbor')], default='select_option', max_length=30),
        ),
    ]
