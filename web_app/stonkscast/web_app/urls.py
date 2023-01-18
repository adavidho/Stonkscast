from django.urls import path

from . import views

# Plain URL leads to Dashboard
urlpatterns = [
    path('', views.index, name='index'),
]