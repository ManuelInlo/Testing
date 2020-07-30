from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidates, name='candidates'),
    path('add/', views.candidates_add, name='candidate_add'),
    path('profile/<int:pk>', views.candidates_profile, name='candidate_profile'),
    path('edit/<int:pk>', views.candidates_edit, name='candidate_edit'),   

]