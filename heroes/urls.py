from . import views
from django.urls import path

app_name = 'heroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_hero'),
    path('delete/<int:hero_id>', views.delete, name='delete'),
    path('<int:hero_id>/update/', views.update, name='update'),
]
