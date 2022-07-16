from django.contrib import admin
from .models import Poll, OpenEnd, OpenEnd_Answer, CloseTest, CloseTest_Answer

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'expired_datetime', )

@admin.register(OpenEnd)
class OpenEndAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'id', 'question', )

@admin.register(OpenEnd_Answer)
class OpenEndAnswerAdmin(admin.ModelAdmin):
    list_display = ('q_id', 'id', 'answer', )

@admin.register(CloseTest)
class CloseTestAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'id', 'question', 'radio1', 'radio2', 'radio3', 'radio4', )

@admin.register(CloseTest_Answer)
class CloseTestAnswerAdmin(admin.ModelAdmin):
    list_display = ('q_id', 'id', 'answer', )
