from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
class Direction_of_studying(models.Model):
    direction = models.CharField(max_length=255, blank=False, unique=True, verbose_name="Направление подготовки")

    def __str__(self):
        return self.direction

    class Meta:
        verbose_name = "Направление подготовки"
        verbose_name_plural = "Направления подготовки"


class Subject(models.Model):
    subject_name = models.CharField(max_length=255, blank=False, unique=True, verbose_name="Предмет")
    direction_name = models.ForeignKey(Direction_of_studying,
                                       on_delete=models.CASCADE,
                                       blank=False,
                                       verbose_name="Направление",
                                       related_name='get_dir')

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"


class Curator(models.Model):
    first_name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
    last_name = models.CharField(max_length=50, blank=False, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, blank=True, verbose_name="Отчество")
    direction_of_studying = models.OneToOneField(Direction_of_studying,
                                                 on_delete=models.SET_NULL,
                                                 null=True,
                                                 verbose_name="Направление",
                                                 related_name='get_curator',)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Куратор", blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Куратор"
        verbose_name_plural = "Кураторы"


class Student(models.Model):
    first_name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
    last_name = models.CharField(max_length=50, blank=False, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, blank=True, verbose_name="Отчество")
    studying_group = models.ForeignKey("Education_group",
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       blank=True,
                                       verbose_name="Учебная группа",
                                       )

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class Education_group(models.Model):
    group_number = models.IntegerField(unique=True,
                                       validators=[MinValueValidator(limit_value=1),
                                                   MaxValueValidator(limit_value=500)],
                                       blank=False,
                                       verbose_name="Номер группы")
    direction = models.ForeignKey("Direction_of_studying", on_delete=models.CASCADE, blank=False,
                                  verbose_name="Направление")

    def __str__(self):
        return str(self.group_number)

    class Meta:
        verbose_name = "Учебная группа"
        verbose_name_plural = "Учебные группы"
