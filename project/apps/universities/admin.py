from django.contrib import admin

from .models import (University, Department, Cycle, Degree, Program, StudyYear,
                     Method)


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Cycle)
class CycleAdmin(admin.ModelAdmin):
    pass


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass


@admin.register(StudyYear)
class StudyYearAdmin(admin.ModelAdmin):
    pass


@admin.register(Method)
class MethodAdmin(admin.ModelAdmin):
    pass
