from django.urls import path,include
from hello import views
urlpatterns = [
    path('hello/',views.index,name='index'),
]