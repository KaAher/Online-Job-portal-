# Generated by Django 5.1.6 on 2025-03-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pd1', '0002_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.CharField(default='default@email.com', max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
