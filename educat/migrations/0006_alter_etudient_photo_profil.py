# Generated by Django 5.1.7 on 2025-03-22 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educat', '0005_alter_groupe_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudient',
            name='photo_profil',
            field=models.FileField(blank=True, null=True, upload_to='profil_prof/%Y/%m/%d/'),
        ),
    ]
