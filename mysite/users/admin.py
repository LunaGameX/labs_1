from django.contrib import admin
from .models import CustomUser, Choice, Question, Answer


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
    exclude = ['user']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    readonly_fields = ()


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser)
