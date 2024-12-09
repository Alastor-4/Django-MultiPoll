from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from .models import Poll, Question, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 0
    fields = ('text', 'image')

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    fields = ('text', 'image')

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("title", "export_button")
    search_fields = ("title",)
    list_filter = ("title",)

    def export_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Export Results</a>',
            reverse("export_results", args=[obj.id])
        )
    export_button.short_description = "Export Results"

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "poll")
    list_filter = ("poll",)
    search_fields = ("text",)
    inlines = [OptionInline]
#
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ("poll", "username", "submitted_at")
#     list_filter = ("poll", "submitted_at")
#     search_fields = ("username",)
#
# class CustomAnswerAdmin(admin.ModelAdmin):
#     list_display = ("answer", "question", "answer")
#     list_filter = ("question",)
#
# class SelectedOptionAdmin(admin.ModelAdmin):
#     list_display = ("answer", "question", "option")
#     list_filter = ("question", "option")

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Option)
# admin.site.register(Answer, AnswerAdmin)
# admin.site.register(CustomAnswer, CustomAnswerAdmin)
# admin.site.register(SelectedOption, SelectedOptionAdmin)