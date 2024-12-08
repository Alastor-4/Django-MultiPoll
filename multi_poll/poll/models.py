from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    poll = models.ForeignKey(Poll, related_name="questions", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.poll.title} - Q{self.id} - {self.text}'

class Option(models.Model):
    question = models.ForeignKey(Question, related_name="options", on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Answer(models.Model):
    poll = models.ForeignKey(Poll, related_name='answer', on_delete=models.CASCADE)
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