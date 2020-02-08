from django.contrib import admin

from .models import Question, Select

admin.site.site_header = "Ez Polling Admin"
admin.site.site_title = "Ez Polling Admin Area"
admin.site.index_title = "Welcome to the Ez Polling admin area"


class SelectInline(admin.TabularInline):
    model = Select
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['published_date'], 'classes': ['collapse']}), ]
    inlines = [SelectInline]


admin.site.register(Question, QuestionAdmin)

# admin.site.register(Question)
# admin.site.register(Select)
