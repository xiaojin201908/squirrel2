from django.urls import path
from . import views

app_name = 'squirrel'
urlpatterns = [
        path('',views.all_list,name='all_list'),
        path('add/',views.add, name='add'),
        path('stats/',views.stats,name='stats'),
        path('<str:unique_squirrel_id>/', views.update,name='update'),
        ]
