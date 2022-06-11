# Generated by Django 4.0.5 on 2022-06-11 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_update_at_jsondata_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=50, verbose_name='command')),
            ],
        ),
        migrations.CreateModel(
            name='Hostname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, verbose_name='hostname')),
            ],
        ),
        migrations.CreateModel(
            name='LogData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('data', models.JSONField(null=True)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.command')),
                ('hostname', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.hostname')),
            ],
        ),
    ]
