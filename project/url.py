from django.urls import path
from django.urls.resolvers import URLPattern
from . import views



urlpatterns = [
    path('',views.projects, name='projects'),
    path('single-project/<str:pk>/',views.singleProject,name='single-project'),
    path('add-project', views.addProject, name='add-project'),
    path('update-project/<str:pk>/', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>/',views.deleteProject, name='delete-project')
    
]