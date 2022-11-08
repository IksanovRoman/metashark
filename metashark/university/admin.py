from django.contrib import admin

from .models import *


# Register your models here.
class Direction_of_studyingAdmin(admin.ModelAdmin):
    list_display = ("direction",)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subject_name", "direction")
    ordering = ["direction", ]


class CuratorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "patronymic", "direction_of_studying")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "patronymic", "studying_group")


class Education_groupAdmin(admin.ModelAdmin):
    list_display = ("group_number", "direction")
    ordering = ["group_number", ]


admin.site.register(Direction_of_studying, Direction_of_studyingAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Curator, CuratorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Education_group, Education_groupAdmin)
