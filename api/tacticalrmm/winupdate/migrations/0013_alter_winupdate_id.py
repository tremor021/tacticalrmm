# Generated by Django 4.2.10 on 2024-02-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("winupdate", "0012_auto_20220227_0554"),
    ]

    operations = [
        migrations.AlterField(
            model_name="winupdate",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
