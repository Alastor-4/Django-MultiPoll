from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from .models import Poll, Question, Option, Answer, CustomAnswer, SelectedOption

class OptionInline(admin.TabularInline):
    model = Option
    extra = 2

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("title", "export_button")
    search_fields = ("title",)
    inlines = [QuestionInline]

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

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("poll", "username", "submitted_at")
    list_filter = ("poll", "submitted_at")
    search_fields = ("username",)

class CustomAnswerAdmin(admin.ModelAdmin):
    list_display = ("answer", "question", "answer")
    list_filter = ("question",)

class SelectedOptionAdmin(admin.ModelAdmin):
    list_display = ("answer", "question", "option")
    list_filter = ("question", "option")

admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(CustomAnswer, CustomAnswerAdmin)
admin.site.register(SelectedOption, SelectedOptionAdmin)

# from django.contrib import admin
# from .models import Poll, Answer, Option, Question, SelectedOption, CustomAnswer
#
# class AnswerInline(admin.TabularInline):
#     model = Answer
#     extra = 0
#
# class UserPollAdmin(admin.ModelAdmin):
#     list_display = ('name', 'poll')
#     inlines = [AnswerInline]
#
# class PollAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description')
#     search_fields = ['title']
#
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('text', 'poll', 'type')
#     search_fields = ['text']
#
# class OptionAdmin(admin.ModelAdmin):
#     list_display = ('text', 'question')
#     search_fields = ['text']
#
# admin.site.register(Poll, PollAdmin)
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Option, OptionAdmin)
# admin.site.register(UserPoll, UserPollAdmin)