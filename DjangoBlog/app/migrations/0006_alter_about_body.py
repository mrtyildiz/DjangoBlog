# Generated by Django 4.1.4 on 2022-12-16 22:12

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_topics_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='body',
            field=mdeditor.fields.MDTextField(blank=True, null=True),
        ),
    ]
