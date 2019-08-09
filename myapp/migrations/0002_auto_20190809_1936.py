# Generated by Django 2.1.8 on 2019-08-09 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtubejobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 8, 9, 19, 36, 2, 624941), verbose_name='date published')),
                ('writer', models.CharField(max_length=50)),
                ('key', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Issue',
        ),
    ]