from django.urls import path
from .views import WorkerListCreate, WorkerRetrieveUpdateDestroy

urlpatterns = [
    path('workers/', WorkerListCreate.as_view(), name='worker-list-create'),
    path('workers/<int:pk>/', WorkerRetrieveUpdateDestroy.as_view(), name='worker-retrieve-update-destroy'),
]
