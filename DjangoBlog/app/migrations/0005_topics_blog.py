# Generated by Django 4.1.4 on 2022-12-16 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_about_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TopicsName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HeaderImage', models.ImageField(upload_to='Blog')),
                ('HeaderName', models.CharField(max_length=25)),
                ('body', models.TextField()),
                ('filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.topics')),
            ],
        ),
    ]