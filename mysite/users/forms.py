from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Question
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'avatar', 'user_info')


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'avatar', 'user_info')


class AddQuestion(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_text', 'full_info', 'short_info', 'question_image')
