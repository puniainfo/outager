# Generated by Django 3.2.10 on 2021-12-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OutageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_from', models.CharField(max_length=100)),
                ('application_name', models.CharField(max_length=100)),
                ('outage_start_time', models.DateTimeField()),
                ('outage_end_time', models.DateTimeField(blank=True, null=True)),
                ('outage_time', models.IntegerField(default=0)),
                ('outage_status', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'outage_model',
            },
        ),
    ]
