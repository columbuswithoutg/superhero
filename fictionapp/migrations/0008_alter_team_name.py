# Generated by Django 5.0 on 2023-12-31 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fictionapp', '0007_alter_team_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, choices=[('Avengers', 'Avengers'), ('Justice League', 'Justice League')], max_length=50, null=True),
        ),
    ]
