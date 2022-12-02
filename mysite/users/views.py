from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm, AddQuestion
from .models import Question, CustomUser, Choice, Answer


class Register(CreateView):
    """Класс регистрации юзера"""
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class DeleteUserView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = CustomUser
    template_name = 'personal_area/delete_user.html'
    success_url = reverse_lazy('index')

    def form_valid(self):
        self.object.delete()


class UpdateUser(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'personal_area/update_user.html'
    success_url = reverse_lazy('personal_area')


class IndexView(ListView):
    model = Question
    paginate_by = 4
    template_name = 'index.html'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class QuestionFullView(DetailView):
    model = Question
    template_name = 'questions/info_question.html'


class QuestionAdd(LoginRequiredMixin, CreateView):
    model = Question
    form_class = AddQuestion
    template_name = 'questions/add_question.html'
    success_url = reverse_lazy('index')


class PersonalAreaView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = CustomUser
    template_name = 'personal_area/personal_area.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'questions/results_question.html'


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect('index.html')


def logout_view(request):
    logout(request)
    redirect('index.html')


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.POST.get('choice', None) is None:
        return render(request, 'questions/info_question.html', {
            'error_message': 'вы не сделали выбор',
            'question': question,
        })
    try:
        user_answer = Answer.objects.get(question_id=question_id,
                                         user_id=request.user.id)
        return render(request, 'questions/info_question.html', {
            'question': user_answer.question,
            'error_message': 'вы уже проголосовали'
        })
    except Answer.DoesNotExist:
        Answer.objects.create(question_id=question_id, user_id=request.user.id)
        return HttpResponseRedirect(reverse('result_question', args=[question_id]))
