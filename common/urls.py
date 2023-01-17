from django.urls import path

from .views import CurrentDateView, IndexView, IndexViewLogin


urlpatterns = [
   path('', IndexView.as_view()),
   path('datetime/', CurrentDateView.as_view()),
   path('', IndexViewLogin.as_view()),
]# 'datetime/' путь по которому будем обрабатывать