# Generated by Django 4.2.3 on 2023-07-23 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TopMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name1', models.CharField(max_length=50)),
                ('country1_flag', models.ImageField(upload_to='')),
                ('country_name2', models.CharField(max_length=50)),
                ('country2_flag', models.ImageField(upload_to='')),
                ('date', models.DateTimeField()),
                ('odd_home', models.FloatField(null=True)),
                ('odd_draw', models.FloatField(null=True)),
                ('odd_away', models.FloatField(null=True)),
                ('comp_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.league')),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.league')),
            ],
        ),
    ]
