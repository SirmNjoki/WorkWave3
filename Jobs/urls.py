
from django.contrib import admin
from django.urls import path
from Jobs import views

urlpatterns = [

    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    # path('applicant/', views.applicant_dashboard, name='applicant'),
    path('employer/', views.employer_dashboard, name='employer'),
    # path('application/<int:application_id>', views.apply_for_job, name='application'),
    # path('job/<int:job_id>/', views.job_detail, name='job'),

]
