from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth import authenticate, login, logout
from quiz.models import Exams, Quiz

# Create your views here.


def RegisterView(request):
    msg = None
    success = None
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            success = 'Muaffaqiyatli ro\'yhatdan o\'tdingiz!'
            return redirect('login')
        else:
            msg = 'Forma notog\'ri to\'ldirilgan!'
    else:
        form = forms.SignUpForm()

    context = {
        'form': form,
        'msg': msg,
        'success': success
    }
    return render(request, 'register.html', context)


def LoginView(request):
    form = forms.LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                msg = 'Login yoki parol xato, qayta urinib ko\'ring'
        else:
            msg = 'Login yoki parol xato, qayta urinib ko\'ring'

    context = {
        'form': form,
        'msg': msg
    }
    return render(request, 'login.html', context)


@login_required
def LogoutView(request):
    logout(request)
    return redirect("home")


def HomeView(request):
    return render(request, 'home.html')


def ProfileView(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    full_name = f"{first_name} {last_name}"
    exams = Exams.objects.filter(author=full_name)
    for exam in exams:
        quizs = Quiz.objects.filter(exam=exam)
        if exam.questions_count >= quizs.count():
            print(quizs.count())
            print(exam.questions_count)
            exam.status = "close"
            exam.save()

    context = {
        'exams': exams
    }
    return render(request, 'profile.html', context)


def edit_profile_view(request):
    user = models.User.objects.get(id=request.user.id)
    if request.method == "POST":
        user.bio = request.POST.get('bio')
        profile_image = request.FILES.get('profile_image')
        if profile_image is not None:
            user.image = profile_image
            print(profile_image)
        user.save()
        return redirect("profile")
    return render(request, 'profile_edit.html', {"user": user})
