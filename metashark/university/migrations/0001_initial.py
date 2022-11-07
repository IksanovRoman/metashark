# Generated by Django 4.1.3 on 2022-11-07 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction_of_studying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction_of_studying', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=255, unique=True)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.direction_of_studying')),
            ],
        ),
        migrations.CreateModel(
            name='Curator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(blank=True, max_length=50)),
                ('direction_of_studying', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='university.direction_of_studying')),
            ],
        ),
    ]
