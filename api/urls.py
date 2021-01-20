from django.urls import path
from .views import *
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/', apiOverview, name='api-overview'),
    path('api/task-list/', taskList, name='task-list'),
    path('api/task-detail/<str:pk>/', taskDetail, name='task-detail'),
    path('api/task-create/', taskCreate, name='task-create'),
    path('api/task-update/<str:pk>/', taskUpdate, name="task-update"),
    path('api/task-delete/<str:pk>/', taskDelete, name="task-delete"),
]
