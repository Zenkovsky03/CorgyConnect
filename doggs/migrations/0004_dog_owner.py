# Generated by Django 5.0.2 on 2024-02-18 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doggs', '0003_dog_featured_image'),
        ('users', '0002_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
