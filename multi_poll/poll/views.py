from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from pipenv.core import console
from .models import Poll, Answer, Option, SelectedOption
import pandas as pd

def poll_list(request):
    poll = Poll.objects.all()
    return render(request, 'poll_list.html', {'poll_list' : poll})

def complete_poll(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    if request.method == 'POST':
        username = request.POST.get('username')
        answer = Answer.objects.create(poll=poll, username=username)

        for question in poll.questions.all():
            option_id = request.POST.get(f'question-{question.id}')
            custom_answer = request.POST.get(f'custom_answer-{question.id}')

            if option_id:
                option = Option.objects.get(id=option_id)
                SelectedOption.objects.create(answer=answer, question=question, option=option)
            elif custom_answer:
                SelectedOption.objects.create(answer=answer, question=question, custom_answer=custom_answer)

        return redirect('/')
    return render(request, 'complete_poll.html', {'poll' : poll})

def export_results(request, poll_id):
    poll = get_object_or_404(Poll, id=poll_id)
    results = Answer.objects.filter(poll=poll)
    data = []
    for result in results:
        row = {"Username" : result.username}
        print(result.custom_answers.all())
        print(result.selected_options.all())
        for question in poll.questions.all():
            selected_option = result.selected_options.filter(question=question).first()
            custom_answer = result.custom_answers.filter(question=question).first()


            row[question.text] = (selected_option.option.text if selected_option else custom_answer.custom_answer if custom_answer else 'No answer')

        data.append(row)

    # df = pd.DataFrame(data, columns=['Name'] + [question.text for question in poll.questions.all()])
    df = pd.DataFrame(data)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    # response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={poll.title}_results.xlsx'
    df.to_excel(response, index=False)
    return response