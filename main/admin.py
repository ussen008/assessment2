from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email', 'username', 'lesson', 'is_staff', ] # new
    fieldsets = UserAdmin.fieldsets + ( # new
    (None, {'fields': ('lesson',)}),
)

    add_fieldsets = UserAdmin.add_fieldsets + ( # new
    (None, {'fields': ('lesson',)}),
)
admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.

admin.site.register(ComprehensiveControl)
admin.site.register(Lesson)
admin.site.register(CategoryClass)
admin.site.register(OrganizeStudy)
admin.site.register(Resources)
admin.site.register(Teaching)
admin.site.register(PlanningLesson)