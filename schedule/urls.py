from django.urls import path, include
from .views import helloAPI,ScheduleAPIView,ScheduleDeleteAPIView,ScheduleCreateAPIView


urlpatterns = [
    path('hello/', helloAPI),
    path('', ScheduleAPIView.as_view()),
    path('<int:pk>/',ScheduleAPIView.as_view()),
    path('add/',ScheduleCreateAPIView.as_view()),
    path('delete/<int:pk>/',ScheduleDeleteAPIView.as_view()),
]
