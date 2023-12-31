# Generated by Django 4.2.7 on 2023-11-29 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0007_delete_customuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_applicant',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('applicant', 'applicant'), ('employer', 'employer')], default='applicant', max_length=20),
            preserve_default=False,
        ),
    ]
