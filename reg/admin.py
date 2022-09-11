from django.contrib import admin

from .models import Subject, Student, Apply
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id_sj", "name_sj", "sem_sj","year_sj", "seat_sj", "status")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id_stu", "name_stu")

class ApplyAdmin(admin.ModelAdmin):
    list_display = ("id_stu", "id_sj")


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Apply, ApplyAdmin)