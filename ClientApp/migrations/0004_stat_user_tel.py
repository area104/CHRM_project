# Generated by Django 4.1.5 on 2023-01-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ClientApp", "0003_remove_stat_user_id_stat_user_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="stat_user",
            name="tel",
            field=models.CharField(default="SOME STRING", max_length=140),
        ),
    ]
