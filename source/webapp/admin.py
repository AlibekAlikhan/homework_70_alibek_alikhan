from django.contrib import admin

from webapp.models import Article, Status, Teg


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "create_at")
    list_filter = ("id", "status", "create_at")
    search_fields = ("status", "text")
    filter = ("text", "status", "create_at")
    readonly_fields = ("id", "create_at")


class StatusAdmin(admin.ModelAdmin):
    search_fields = ["status"]
    filter = ["status"]
    readonly_fields = ["id"]


class TegAdmin(admin.ModelAdmin):
    search_fields = ["teg"]
    filter = ["teg"]
    readonly_fields = ["id"]


admin.site.register(Status, StatusAdmin)
admin.site.register(Teg, TegAdmin)
admin.site.register(Article, ArticleAdmin)
