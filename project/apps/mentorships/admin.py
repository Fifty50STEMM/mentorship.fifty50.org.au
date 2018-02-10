from django.contrib import admin

from .models import (Session, SessionWeek, UserRole, UserDegree, UniversitySession,
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
class UserDegreeInline(admin.TabularInline):

    model = UserDegree
    extra = 1


class UserRoleInline(admin.TabularInline):

    model = UserRole
    extra = 1




@admin.register(UserUniversity)
class UserUniversityAdmin(admin.ModelAdmin):

    inlines = [UserDegreeInline, UserRoleInline]


@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    pass


@admin.register(UserRole)
class UserRole(admin.ModelAdmin):

    list_display = ['university_session', 'user',
                    'role', 'is_active', 'relationship', 'notes']
    list_filter = ['university_session', 'role', 'is_active', 'user']
    list_search = ['user']


admin.site.site_header = 'Fifty50 Mentoring Administration'
