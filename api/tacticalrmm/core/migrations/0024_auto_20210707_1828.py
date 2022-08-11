# Generated by Django 3.2.1 on 2021-07-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_coresettings_clear_faults_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='coresettings',
            name='agent_history_prune_days',
            field=models.PositiveIntegerField(default=30),
        ),
        migrations.AddField(
            model_name='coresettings',
            name='resolved_alerts_prune_days',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
