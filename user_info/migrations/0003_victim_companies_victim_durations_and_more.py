# Generated by Django 4.1.7 on 2023-03-10 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0002_alter_victim_about_alter_victim_current_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='victim',
            name='companies',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='victim',
            name='durations',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='victim',
            name='github_repos',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='victim',
            name='institutions',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='victim',
            name='job_descriptions',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='victim',
            name='positions',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='victim',
            name='tenures',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='victim',
            name='victim_skills',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='victim',
            name='about',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='victim',
            name='current_position',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='victim',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='victim',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
