from django.urls import path
from . import views

urlpatterns=[
    path('home',views.schoolAdmin_home),
    path('viewstaff',views.schoolAdmin_viewstaff),
    path('addstaff',views.schoolAdmin_addstaff),
    path('viewstudent',views.schoolAdmin_viewstudent)
]