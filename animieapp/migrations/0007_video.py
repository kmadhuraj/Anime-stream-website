# Generated by Django 3.2.22 on 2023-10-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animieapp', '0006_rename_signup_signups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video', models.FileField(upload_to='vdo')),
                ('image', models.ImageField(upload_to='img')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('type', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('genre', models.TextField()),
                ('country', models.CharField(max_length=50)),
                ('score', models.DecimalField(decimal_places=2, max_digits=3)),
                ('duration', models.IntegerField()),
                ('episodes', models.IntegerField()),
            ],
        ),
    ]
