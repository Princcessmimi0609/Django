# Generated by Django 5.1.2 on 2024-10-14 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_alter_attendance_attendance_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='id',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_number',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
