# Generated by Django 5.1.6 on 2025-02-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pd1', '0003_apply_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apply',
            old_name='job_role',
            new_name='city',
        ),
        migrations.AddField(
            model_name='apply',
            name='email',
            field=models.CharField(default='Not Specified', max_length=200),
        ),
        migrations.AddField(
            model_name='apply',
            name='resume',
            field=models.FileField(default='default@email.com', upload_to='resumes/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apply',
            name='role',
            field=models.CharField(default='default@email.com', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='apply',
            name='company_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='company_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default='default@email.com', max_length=200),
        ),
    ]
