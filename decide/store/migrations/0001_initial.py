# Generated by Django 4.1 on 2023-11-27 17:52

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voting_id', models.PositiveIntegerField()),
                ('voter_id', models.PositiveIntegerField()),
                ('question_id', models.PositiveIntegerField(null=True)),
                ('a', base.models.BigBigField()),
                ('b', base.models.BigBigField()),
                ('voted', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
