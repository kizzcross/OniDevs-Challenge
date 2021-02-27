from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_form,name='music_insert'), # get and post req. for insert operation
    path('<int:id>/', views.music_form,name='music_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.music_delete,name='music_delete'),
    path('list/',views.music_list,name='music_list') # get req. to retrieve and display all records
]