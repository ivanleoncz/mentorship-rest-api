# Generated by Django 3.1.2 on 2020-10-12 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20201012_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorship',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('disabled', 'Disabled')], default='active', max_length=12),
        ),
    ]