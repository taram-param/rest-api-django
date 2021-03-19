from django.contrib import admin

from .models import Fundraising, Fee


@admin.register(Fundraising)
class FundraisingAdmin(admin.ModelAdmin):
    list_display = ("title", "description",)


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ("user", "fundraising")
    list_display_links = ("user",)

