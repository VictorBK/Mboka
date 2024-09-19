from django.urls import path

from . import views


urlpatterns = [
    path('newest/', views.NewestJobsView.as_view()),
]