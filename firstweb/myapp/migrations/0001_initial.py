# Generated by Django 5.0.6 on 2024-05-12 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('tracking', models.CharField(blank=True, max_length=100, null=True)),
                ('other', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
