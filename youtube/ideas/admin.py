from django.contrib import admin

# Register your models here.

from .models import Idea, Vote

admin.site.register(Idea)
admin.site.register(Vote)

