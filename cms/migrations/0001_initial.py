# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('tags', models.CharField(max_length=100)),
                ('views_count', models.TextField()),
                ('comments_count', models.TextField()),
                ('auth', models.TextField(default=b'\xe8\xb0\xb7\xe6\x99\xa8')),
                ('address', models.CharField(default=b'\xe8\xa5\xbf\xe5\xae\x89', max_length=100)),
            ],
        ),
    ]
