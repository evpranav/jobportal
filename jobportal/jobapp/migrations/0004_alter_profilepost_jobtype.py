# Generated by Django 4.1.1 on 2022-10-02 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_rename_postjob_profilepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepost',
            name='jobtype',
            field=models.CharField(choices=[('parttime', 'part_time'), ('fulltime', 'full_time')], max_length=20),
        ),
    ]
