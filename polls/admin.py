from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "County Polls Admin"
admin.site.site_title = "County Polls Admin Area"
admin.site.index_title = "Welcome to the County Polls admin area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)