from django.urls import path
from . import views
from .views import Register, PersonalAreaView, DeleteUserView, UpdateUser, QuestionAdd, IndexView, \
    QuestionFullView

urlpatterns = [
    path('', IndexView.as_view(template_name="index.html"), name='index'),
    path('signup/', Register.as_view(), name='signup'),
    path('personal_area/', PersonalAreaView.as_view(), name='personal_area'),
    path('delete_user/<int:pk>/', DeleteUserView.as_view(), name='delete_user'),
    path('update_user/<int:pk>/', UpdateUser.as_view(), name='update_user'),
    path('create_question/', QuestionAdd.as_view(), name='add_question'),
    path('question_info/<int:pk>/', QuestionFullView.as_view(), name='info_question'),
    path('vote/<int:question_id>/', views.vote, name='vote'),
    path('result/<int:pk>/', views.ResultsView.as_view(), name='result_question'),
]
