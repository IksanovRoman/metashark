from django.db import models


# Create your models here.
class Direction_of_studying(models.Model):
    direction_of_studying = models.CharField(max_length=255, blank=False, unique=True, verbose_name="Направление подготовки")

    def __str__(self):
        return self.direction_of_studying

    class Meta:
        verbose_name = "Направление подготовки"
        verbose_name_plural = "Направления подготовки"


class Subject(models.Model):
    subject_name = models.CharField(max_length=255, blank=False, unique=True, verbose_name="Предмет")
    direction = models.ForeignKey(Direction_of_studying,
                                  on_delete=models.CASCADE,
                                  blank=False,
                                  verbose_name="Направление")

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
                                                 blank=True,
                                                 null=True,
                                                 verbose_name="Направление")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = "Куратор"
        verbose_name_plural = "Кураторы"


# class Student(models.Model):
#     first_name = models.CharField(max_length=50, blank=False, verbose_name="Имя")
#     last_name = models.CharField(max_length=50, blank=False, verbose_name="Фамилия")
#     patronymic = models.CharField(max_length=50, blank=True, verbose_name="Отчество")
#     studying_group = models.OneToOneField("Group", on_delete)
