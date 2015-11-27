# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='field_types',
            fields=[
                ('ty_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('open_tag', models.CharField(max_length=100)),
                ('options', models.CharField(max_length=100)),
                ('close_tag', models.CharField(default=b'nill', max_length=100)),
                ('active', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='fields',
            fields=[
                ('fd_id', models.AutoField(serialize=False, primary_key=True)),
                ('position', models.IntegerField()),
                ('label', models.CharField(max_length=300)),
                ('options', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Forms',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('uniq_url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=400)),
                ('description', models.CharField(max_length=1500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='fields',
            name='fm_id',
            field=models.ForeignKey(to='formgen.Forms'),
        ),
        migrations.AddField(
            model_name='fields',
            name='ty_id',
            field=models.ForeignKey(to='formgen.field_types'),
        ),
    ]
