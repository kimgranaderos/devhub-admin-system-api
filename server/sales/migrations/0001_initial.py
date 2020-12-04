# Generated by Django 3.1.4 on 2020-12-04 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoWorkingSpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space_name', models.CharField(max_length=20, unique=True)),
                ('hour', models.SmallIntegerField()),
                ('whole_day', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=30, unique=True)),
                ('co_working', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sales.coworkingspace')),
            ],
        ),
    ]
