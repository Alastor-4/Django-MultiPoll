from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Poll, Answer, Option, Question, SelectedOption, CustomAnswer
import pandas as pd

def poll_list(request):
    poll = Poll.objects.filter(
        is_active=True,
        questions__isnull=False,
        questions__options__isnull=False
    ).distinct()
    return render(request, 'poll_list.html', {'poll_list': poll})

def complete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)

    if request.method == 'POST':
        username = request.POST.get('username')

        answer = Answer.objects.filter(poll=poll, username=username)
        if answer:
            answer.delete()

        answer = Answer.objects.create(poll=poll, username=username)

        for question in poll.questions.all():
            option_id = request.POST.get(f'option-{question.id}')
            custom_answer = request.POST.get(f'custom_answer_input-{question.id}')
            if option_id:
                option = Option.objects.get(id=option_id)
                SelectedOption.objects.create(answer=answer, question=question, option=option)
            elif custom_answer:
                CustomAnswer.objects.create(answer=answer, question=question, custom_answer=custom_answer)

        return redirect('/')
    return render(request, 'complete_poll.html', {
        'poll': poll,
        'total_questions': poll.questions.count(),
        'progress': 0
    })

def export_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    results = Answer.objects.filter(poll=poll)
    data = []
    for result in results:
        row = {"Username" : result.username}
        for question in poll.questions.all():
            selected_option = result.selected_options.filter(question=question).first()
            custom_answer = result.custom_answers.filter(question=question).first()

            row[question.text] = (selected_option.option.text if selected_option else custom_answer)

        data.append(row)

    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename={poll.title}-results.xlsx'
    df.to_excel(response, index=False)
    return response

def toggle_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    poll.is_active = not poll.is_active
    poll.save()
    return HttpResponse(status=204)

def delete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    poll.delete()
    return HttpResponse(status=204)

def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return HttpResponse(status=204)

def delete_option(request, option_id):
    option = get_object_or_404(Option, id=option_id)
    option.delete()
    return HttpResponse(status=204)