# Generated by Django 5.1.6 on 2025-02-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=500)),
                ('email', models.CharField(default='Not Specified', max_length=200)),
                ('name', models.CharField(default='Anonymous', max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=500)),
                ('job_role', models.CharField(max_length=200)),
                ('email', models.CharField(default='default@email.com', max_length=200)),
                ('salary', models.IntegerField()),
                ('description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='default@email.com', max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Userjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='default@email.com', max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
