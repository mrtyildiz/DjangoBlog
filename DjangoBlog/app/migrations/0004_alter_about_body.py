# Generated by Django 4.1.4 on 2022-12-16 19:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_about_profil_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
