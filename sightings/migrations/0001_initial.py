# Generated by Django 3.0 on 2019-12-05 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=15, help_text='Latitude', max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=15, help_text='Longitude', max_digits=20)),
                ('unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=50)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Shift', max_length=3)),
                ('date', models.DateField(default=django.utils.timezone.now, help_text='Date')),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age', max_length=10)),
                ('primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='Primary Fur Color', max_length=10)),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='Location', max_length=20)),
                ('specific_location', models.CharField(blank=True, help_text='Specific Location', max_length=100, null=True)),
                ('running', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Running', max_length=15)),
                ('chasing', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Chasing', max_length=15)),
                ('climbing', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Climbing', max_length=15)),
                ('eating', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Eating', max_length=15)),
                ('foraging', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Foraging', max_length=15)),
                ('other_activities', models.CharField(blank=True, help_text='Other Activities', max_length=100, null=True)),
                ('kuks', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Kuks', max_length=15)),
                ('quaas', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Quaas', max_length=15)),
                ('moans', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Moans', max_length=15)),
                ('tail_flags', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Tail Flags', max_length=15)),
                ('tail_twitches', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Tail Twitches', max_length=15)),
                ('approaches', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Approaches', max_length=15)),
                ('indifferent', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Indifferent', max_length=15)),
                ('runs_from', models.CharField(choices=[('true', 'True'), ('false', 'False')], help_text='Runs From', max_length=15)),
            ],
        ),
    ]
