# Generated by Django 2.2.19 on 2021-07-19 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceType', models.CharField(max_length=200)),
                ('localisation', models.CharField(max_length=200)),
                ('capacity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=200)),
                ('firstName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleB', models.CharField(max_length=500)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourceManagement.Resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourceManagement.Users')),
            ],
        ),
    ]