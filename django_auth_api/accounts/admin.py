from django.contrib import admin
from accounts.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ["gender", "age", "created_at"]
    list_display = ["name", "surname", "gender", "age", "created_at", "state", "city"]
    search_fields = ["name", "surname"]
    readonly_fields = ["api_key"]


admin.site.register(CustomUser, CustomUserAdmin)