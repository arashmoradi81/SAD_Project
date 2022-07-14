from django.contrib import admin
from .models import Poll, OpenEnd


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'expired_datetime', )

@admin.register(OpenEnd)
class OpenEndAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'id', 'question', )

