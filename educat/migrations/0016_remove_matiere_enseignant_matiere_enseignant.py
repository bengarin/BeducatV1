# Generated by Django 5.1.7 on 2025-04-06 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educat', '0015_enseignant_temp_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matiere',
            name='enseignant',
        ),
        migrations.AddField(
            model_name='matiere',
            name='enseignant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='educat.enseignant'),
        ),
    ]
