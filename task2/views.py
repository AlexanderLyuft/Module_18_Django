# from django.shortcuts import render
# from django.views import View
#
# # Классовое представление
# class ClassBasedView(View):
#     def get(self, request):
#         return render(request, 'second_task/class_template.html')
#
# # Функциональное представление
# def func_based_view(request):
#     return render(request, 'second_task/func_template.html')
#

from django.views import View
from django.http import HttpResponse

class ClassBasedView(View):
    def get(self, request):
        return HttpResponse("Hello from Class-Based View!")

def func_based_view(request):
    return HttpResponse("Hello from Function-Based View!")