# Generated by Django 5.0.1 on 2024-06-28 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_expertfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calnoti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('USER', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
