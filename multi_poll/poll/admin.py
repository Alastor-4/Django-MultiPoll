from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html
from .models import Poll, Question, Option
from unfold.admin import ModelAdmin

# admin.site.site_header = 'MultiPoll Website'
# admin.site.site_title = 'MultiPoll Admin Site'

@admin.register(Poll)
class PollAdmin(ModelAdmin):
    list_display = ("title", "description", "publish_date", "image_preview", "total_answers", "is_active", "toggle_active", "export_button", "delete_button")
    list_display_links = ("title",)
    search_fields = ("title", "description")
    readonly_fields = ("image_preview",)
    ordering = ("publish_date",)
    list_per_page = 5
    actions = None

    @admin.display(description="Total Answers")
    def total_answers(self, obj):
        return obj.answers.count()

    def export_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Export Results</a>',
            reverse("export_results", args=[obj.id])
        )
    export_button.short_description = "Export Results"

    def delete_button(self, obj):
        return format_html(
            '<a class="button" style="background-color: red;" href="{}">Delete Poll</a>',
            reverse("delete_poll", args=[obj.id])
        )
    delete_button.short_description = "Delete Poll"

    def toggle_active(self, obj):
        return format_html(
            '<a class="button" style="background-color: yellow;" href="{}">Toggle Active</a>',
            reverse("toggle_poll", args=[obj.id])
        )

@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("text", "poll", "image", "image_preview", "delete_button")
    search_fields = ("text",)
    autocomplete_fields = ("poll",)
    list_per_page = 5
    actions = None

    def delete_button(self, obj):
        return format_html(
            '<a class="button" style="background-color: red; padding: 4px 6px; border-radius: 5px; color: white; font-weight: 600;" href="{}">Delete Question</a>',
            reverse("delete_question", args=[obj.id])
        )

    delete_button.short_description = "Delete Question"


@admin.register(Option)
class OptionAdmin(ModelAdmin):
    list_display = ('text', 'question', "image_preview", "delete_button")
    search_fields = ("text",)
    autocomplete_fields = ("question",)
    list_per_page = 5
    actions = None

    def delete_button(self, obj):
        return format_html(
            '<a class="button" style="background-color: red; padding: 4px 6px; border-radius: 5px; color: white; font-weight: 600;" href="{}">Delete Option</a>',
            reverse("delete_option", args=[obj.id])
        )

    delete_button.short_description = "Delete Option"
