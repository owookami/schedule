# Generated by Django 4.1.6 on 2023-02-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="schedule", name="date", field=models.DateField(),
        ),
    ]
