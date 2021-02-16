from django.urls import path, include
from basic_app import views

# This is the name we use in the templates to call the urls
app_name='basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('<slug:pk>/', views.SchoolDetailView.as_view(), name='detail'),
]
