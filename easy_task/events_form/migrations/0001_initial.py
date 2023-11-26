# Generated by Django 4.2.7 on 2023-11-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('magnitude', models.DecimalField(decimal_places=2, max_digits=2)),
                ('depth', models.DecimalField(decimal_places=2, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=2)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
    ]