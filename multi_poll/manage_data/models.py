from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe
import os

class Poll(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=255)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/poll/', help_text="Upload an Image to be the part of the Header", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Poll"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.imgage.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.id:
            last_instance = Poll.objects.get(id=self.id)
            if last_instance.image and last_instance.image != self.image:
                if os.path.isfile(last_instance.image.path):
                    os.remove(last_instance.image.path)
        super().save(*args, **kwargs)

    @admin.display(description="Image Preview")
    def image_preview(self):
        return mark_safe(f'<img src="{self.image.url}" alt="" style="object-fit: cover;" height="100" width="100" />' if self.image else f'<p>No Image</p>')

    @admin.display(description="Image")
    def image_list_preview(self):
        return mark_safe(f'<img src="{self.image.url}" alt="" width="60" height="60" style="border: 1px solid #000; border-radius:25%;" />' if self.image else f'<p>No Image</p>')

    def __str__(self):
        return self.title


class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name="questions", on_delete=models.CASCADE)
    text = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/question/', help_text="Upload an Image to better explain the question", null=True, blank=True)

    def __str__(self):
        return f'{self.poll.title} - Q{self.id} - {self.text}'

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.id:
            last_instance = Question.objects.get(id=self.id)
            if last_instance.image and last_instance.image != self.image:
                if os.path.isfile(last_instance.image.path):
                    os.remove(last_instance.image.path)
        super().save(*args, **kwargs)

    @admin.display(description="Image Preview")
    def image_preview(self):
        return mark_safe(
            f'<img src="{self.image.url}" alt="" style="object-fit: cover;" height="100" width="100" />' if self.image else f'<p>No Image</p>')

    @admin.display(description="Image")
    def image_list_preview(self):
        return mark_safe(
            f'<img src="{self.image.url}" alt="" width="60" height="60" style="border: 1px solid #000; border-radius:25%;" />' if self.image else f'<p>No Image</p>')

    class Meta:
        verbose_name_plural = "Questions"

class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/option/', help_text="Upload an Image to better explain the option", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Options"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.imgage.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.id:
            last_instance = Option.objects.get(id=self.id)
            if last_instance.image and last_instance.image != self.image:
                if os.path.isfile(last_instance.image.path):
                    os.remove(last_instance.image.path)
        super().save(*args, **kwargs)

    @admin.display(description="Image Preview")
    def image_preview(self):
        return mark_safe(f'<img src="{self.image.url}" alt="" style="object-fit: cover;" height="60" width="60" />' if self.image else f'<p>No Image</p>',)

    @admin.display(description="Image")
    def image_list_preview(self):
        return mark_safe(f'<img src="{self.image.url}" alt="" width="60" height="60" style="border: 1px solid #000; border-radius:25%;" />' if self.image else f'<p>No Image</p>')

    def __str__(self):
        return f'{self.question.text} - O{self.id} - {self.text}'

class Answer(models.Model):
    poll = models.ForeignKey(Poll, related_name='answers', on_delete=models.CASCADE)
    username = models.CharField(max_length=40)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Answer of {self.username} in {self.poll.title}'

class CustomAnswer(models.Model):
    answer = models.ForeignKey(Answer, related_name="custom_answers", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    custom_answer = models.TextField(max_length=100)

    def __str__(self):
        return self.custom_answer

class SelectedOption(models.Model):
    answer = models.ForeignKey(Answer, related_name="selected_options", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return self.option.text