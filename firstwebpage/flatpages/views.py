from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'static_handler.html')

#this is task 1.1 solution. needed to add charset=UTF-8 to display russian
#def hello(request):
    #return HttpResponse(u'Привет, мир!', content_type="text/plain;charset=UTF-8")

#this is task 1.2 solution
def hello(request):
    return HttpResponse(u'Привет, мир!')
#the difference is in font and size and being able to show russian text without using charset=UTF-8 

# Create your views here.
