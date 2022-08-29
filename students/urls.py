
from django.urls import path
from .views import StudentCreate, StudentsList, StudentDetail, StudentUpdate


urlpatterns = [
    path('create/', StudentCreate.as_view(), name='create-student'),
    path('', StudentsList.as_view()),
    path('<int:pk>/', StudentDetail.as_view(), name='retrieve-student'),
    path('update/<int:pk>/', StudentUpdate.as_view(), name='update-student'),
]
