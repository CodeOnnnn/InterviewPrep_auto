# Generated by Django 4.1.2 on 2022-11-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_response_options_response_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='max_score',
            field=models.FloatField(default=0),
        ),
    ]