# Generated by Django 4.2.11 on 2024-04-03 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agriculture_App', '0004_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor', models.TextField(default=None, max_length=155500, null=True)),
                ('Patient', models.TextField(default=None, max_length=155500, null=True)),
                ('Booking_Date_Time', models.DateTimeField(default=None, max_length=155500, null=True)),
                ('Start_time', models.TimeField(default=None, max_length=100)),
                ('End_Time', models.TimeField(default=None, max_length=100)),
                ('Reason', models.TextField(default=None, max_length=155500, null=True)),
                ('Appointment_Status', models.TextField(default=None, max_length=155500, null=True)),
                ('Updated_Date_Time', models.DateTimeField(default=None, max_length=155500, null=True)),
                ('Prescription', models.TextField(default=None, max_length=155500, null=True)),
                ('Diagnosis', models.TextField(default=None, max_length=155500, null=True)),
                ('Follow_Up_Instructions', models.TextField(default=None, max_length=155500, null=True)),
                ('Speciality_Type', models.TextField(default=None, max_length=155500, null=True)),
                ('Lab_Tests', models.TextField(default=None, max_length=155500, null=True)),
                ('Imaging_Tests', models.TextField(default=None, max_length=155500, null=True)),
                ('Billing_and_Payment', models.TextField(default=None, max_length=155500, null=True)),
                ('Medical_History', models.TextField(default=None, max_length=155500, null=True)),
                ('Treatment_Status', models.TextField(default='Pending', max_length=155500, null=True)),
                ('Fee_status', models.TextField(default='Pending', max_length=155500, null=True)),
            ],
            options={
                'db_table': 'Appointment',
            },
        ),
    ]
