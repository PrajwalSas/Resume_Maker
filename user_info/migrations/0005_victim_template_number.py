# Generated by Django 4.1.7 on 2023-03-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0004_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='victim',
            name='template_number',
            field=models.CharField(default=1, max_length=1),
        ),
    ]