# Generated by Django 4.1.3 on 2022-11-08 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0010_alter_student_studying_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education_group',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.direction_of_studying', verbose_name='Направление'),
        ),
    ]
