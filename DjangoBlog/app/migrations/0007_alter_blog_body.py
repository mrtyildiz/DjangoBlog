# Generated by Django 4.1.4 on 2022-12-16 22:14

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_about_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
    ]
