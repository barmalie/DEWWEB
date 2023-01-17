from random import random

from django.views import View
from django.http import HttpResponse


class CurrentRandomView(View):
   def get(self, request):
       random_number = random()
       html = f"{random_number}"
       return HttpResponse(html)



