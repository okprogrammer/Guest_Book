from django.urls import path,include
from guestbook import views
urlpatterns = [
    path('',views.index,name='index'),
    path('sign/',views.sign,name='sign'),
]