from django.contrib import admin
from notice.models import Notice, Image


class ImageInline(admin.StackedInline):
    model = Image
    fields = ["image"]
    extra = 1
    

class NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields" : ["title", "content", "created_at"]})
    ]
    list_display = ["title", "content", "created_at"]
    search_fields = ["title", "content"]
    readonly_fields = ["created_at"]
    inlines = [ImageInline]


admin.site.register(Notice, NoticeAdmin)