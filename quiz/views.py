from django.shortcuts import render
from accounts.models import Results, Temporary_user
from . import models

# Create your views here.


def ExamsView(request):
    exams = models.Exams.objects.all()
    context = {'exams': exams}
    return render(request, 'home.html', context)


def ExamsDetailView(request, pk):
    choose_exam = models.Exams.objects.get(pk=pk)
    choose_exam_quizes = models.Quiz.objects.filter(exam=pk)
    count_question = len(list(choose_exam_quizes))
    if request.method == "POST":
        questions = models.Quiz.objects.filter(exam=pk).all()
        wrong, correct, total = 0, 0, 0
        user = request.user
        time_out = request.POST.get('timer')
        # TEMPRARY USER
        temprary_first_name = request.POST.get('temprary_first_name')
        temprary_last_name = request.POST.get('temprary_last_name')
        for question in questions:
            total += 1
            print(f'Question: {question.question}')
            print(f'User answer: {request.POST.get(question.question)}')
            print(f'Answer: {question.answer}')
            print(time_out)
            print('--'*20)

            if question.answer == request.POST.get(question.question):
                correct += 1
            else:
                wrong += 1
        # user = request.POST.get('')

        try:
            Results.objects.create(
                user=user,
                exam=choose_exam,
                correct=correct,
                wrong=wrong,
                time_out=time_out
            )
        except:
            Temporary_user.objects.create(
                first_name=temprary_first_name,
                last_name=temprary_last_name,
                exam_name=choose_exam,
                correct=correct,
                wrong=wrong,
                time_out=time_out
            )

        context = {
            "total": total,
            "correct": correct,
            'wrong': wrong,
            'time': time_out,
            'choose_exam': choose_exam
        }
        return render(request, 'results.html', context)

    else:
        context = {'choose_exam': choose_exam,
                   'choose_exam_quizes': choose_exam_quizes,
                   }
        return render(request, 'exams_items.html', context)


def ResultsListView(request, pk):
    choose_exam = models.Exams.objects.get(pk=pk)
    results_user = Results.objects.filter(exam=choose_exam).first()
    results_user_items = [
        results_user.user.first_name,
        results_user.user.last_name,
        results_user.correct,
        results_user.wrong,
        results_user.time_out,
    ]

    results_temrary_users = Temporary_user.objects.filter(
        exam_name=choose_exam
    )

    context = {
        'results': results_user,
        'choose_exam': choose_exam,
        'results_user_items':results_user_items,
        'results_temrary_users': results_temrary_users
    }
    return render(request, 'results_list.html', context)
