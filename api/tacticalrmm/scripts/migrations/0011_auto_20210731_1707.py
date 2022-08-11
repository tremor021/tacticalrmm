# Generated by Django 3.2.1 on 2021-07-31 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0010_auto_20210726_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scriptsnippet',
            name='code',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='scriptsnippet',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='scriptsnippet',
            name='shell',
            field=models.CharField(choices=[('powershell', 'Powershell'), ('cmd', 'Batch (CMD)'), ('python', 'Python')], default='powershell', max_length=15),
        ),
    ]
