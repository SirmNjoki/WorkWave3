# Generated by Django 4.2.7 on 2023-11-29 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0009_remove_userprofile_role_userprofile_is_applicant_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_employee',
            new_name='is_employer',
        ),
    ]
