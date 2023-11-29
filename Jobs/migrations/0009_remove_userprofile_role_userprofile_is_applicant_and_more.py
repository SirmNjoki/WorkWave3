# Generated by Django 4.2.7 on 2023-11-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0008_remove_userprofile_is_applicant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_applicant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]
