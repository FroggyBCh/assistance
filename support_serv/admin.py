from django.contrib import admin
from .models import Problem, Message

class ProblemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "created","owner", "done")
    list_display_links = ("id", "title", "done")
    search_fields = ("id", "title", "description")
    list_filter = ("done",)


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Message)

