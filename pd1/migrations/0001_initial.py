# Generated by Django 5.1.6 on 2025-02-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comapany_name', models.CharField(max_length=200)),
                ('job_role', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
    ]
