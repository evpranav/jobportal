# Generated by Django 4.1.1 on 2023-02-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0008_applyjobmodel1_delete_applyjobmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilepost',
            name='jobtype',
            field=models.CharField(choices=[('parttime', 'parttime'), ('fulltime', 'fulltime')], max_length=20),
        ),
    ]
