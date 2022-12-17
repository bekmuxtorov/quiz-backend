from django.shortcuts import render
from . import models

# Create your views here.


def ExamsView(request):
    exams = models.Exams.objects.all()
    context = {'exams': exams}
    return render(request, 'index.html', context)


def ExamsDetailView(request, pk):
    choose_exam = models.Exams.objects.get(pk=pk)
    choose_exam_quizes = models.Quiz.objects.filter(exam=pk)
    count_question = len(list(choose_exam_quizes))
    if request.method == "POST":
        questions = models.Quiz.objects.filter(exam=pk).all()
        wrong, correct, total = 0, 0, 0
        for question in questions:
            total += 1
            print(f'Question: {question.question}')
            print(f'User answer: {request.POST.get(question.question)}')
            print(f'Answer: {question.answer}')
            print(request.POST.get('timer'))
            print('--'*20)
            
            if question.answer == request.POST.get(question.question):
                correct += 1
            else:
                wrong += 1
        context = {
            "total": total,
            "correct": correct,
            'wrong': wrong,
            'time': request.POST.get('time')
        }
        return render(request, 'results.html', context)

    else:
        context = {'choose_exam': choose_exam,
                   'choose_exam_quizes': choose_exam_quizes,
                   }
        return render(request, 'exams_items.html', context)
