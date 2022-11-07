from django.contrib import admin

from .models import *


# Register your models here.
class Direction_of_studyingAdmin(admin.ModelAdmin):
    list_display = ("direction_of_studying",)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("subject_name", "direction")


class CuratorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "patronymic", "direction_of_studying")


admin.site.register(Direction_of_studying, Direction_of_studyingAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Curator, CuratorAdmin)
