from django.contrib import admin
from django.utils.html import format_html
from notice.models import Notice, Image


class ImageInline(admin.StackedInline):
    model = Image
    fields = ["image"]
    extra = 1
    

class NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields" : ["title", "content", "created_at"]})
    ]
    list_display = ["title", "short_content", "created_at"]
    search_fields = ["title", "content"]
    readonly_fields = ["created_at"]
    inlines = [ImageInline]
    
    def short_content(self, obj):
        return format_html(
            "{}...",
            obj.content[:30] if len(obj.content) > 30 else obj.content
        )
    short_content.short_description = "내용"


admin.site.register(Notice, NoticeAdmin)