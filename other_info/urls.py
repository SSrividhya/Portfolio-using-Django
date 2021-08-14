from django.urls import path
from other_info import views

app_name='other_info'
urlpatterns = [
    path('',views.infos,name='infos'),
    path('<int:info_id>/',views.each_info,name='each_info'),


]
