# Generated by Django 4.2.6 on 2023-11-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=30)),
            ],
        ),
    ]
