from django.urls import path

from .views import CurrentDateView


urlpatterns = [
   path('', IndexView.as_view()),
   path('datetime/', CurrentDateView.as_view()),
]# 'datetime/' путь по которому будем обрабатывать