from django.urls import path

from .views import CurrentRandomView


urlpatterns = [
   path('random/', CurrentRandomView.as_view()),
]# 'datetime/' путь по которому будем обрабатывать