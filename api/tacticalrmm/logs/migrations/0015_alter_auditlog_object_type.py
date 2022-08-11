# Generated by Django 3.2.1 on 2021-07-21 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0014_auditlog_agent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='object_type',
            field=models.CharField(choices=[('user', 'User'), ('script', 'Script'), ('agent', 'Agent'), ('policy', 'Policy'), ('winupdatepolicy', 'Patch Policy'), ('client', 'Client'), ('site', 'Site'), ('check', 'Check'), ('automatedtask', 'Automated Task'), ('coresettings', 'Core Settings'), ('bulk', 'Bulk'), ('alert_template', 'Alert Template'), ('role', 'Role')], max_length=100),
        ),
    ]
