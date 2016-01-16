# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('price', models.TextField()),
                ('quantity', models.TextField()),
                ('picture', models.ImageField(default=b'', upload_to=b'./Pictures/')),
            ],
            options={
                'ordering': ['price'],
            },
        ),
    ]
