from django.contrib import admin
from django.utils.html import format_html
from .models import Idea, Vote

class VoteInline(admin.StackedInline):
    model = Vote
    extra = 0


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'show_youtube_url', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')
    inlines = [VoteInline]

    def show_youtube_url(self, obj):
        return format_html(f'<a href="{obj.youtube_url}" target="_blank">{obj.youtube_url}</a>') if obj.youtube_url else ''

    show_youtube_url.short_description = 'Link'

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'idea__title' , 'reason')
    list_filter = ('idea__title', 'created_at')
    search_fields = ('idea__title', 'reason')

