from django.contrib import admin

from .models import (Session, SessionWeek, UniversitySession,
                     UserUniversity, Relationship)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    pass


@admin.register(SessionWeek)
class SessionWeekAdmin(admin.ModelAdmin):
    pass


@admin.register(UniversitySession)
class UniversitySessionAdmin(admin.ModelAdmin):
    pass


@admin.register(UserUniversity)
class UserUniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    pass
