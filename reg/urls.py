from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('student/', views.student, name='student'),
    path('checkStu/', views.checkStu, name='checkStu'),
    path('checkSub/', views.checkSub, name='checkSub'),
    # path('index/', views.index, name='index'),

    path('rv_index_search/', views.index, name='rv_index_search'),
    path('rv_search/', views.search, name='rv_search'),
    
    path('rv_index_student/', views.index, name='rv_index_student'),
    path('rv_student/', views.student, name='rv_student'),
]