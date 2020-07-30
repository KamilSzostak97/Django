from django.shortcuts import render
from .models import PoliticalViews,IQTest,FastFood
# Create your views here.

def homepage(request):
	return render(request,'quiz/homepage.html')

def politics(request):
    context = {
    'questions': PoliticalViews.objects.all()
    }
    return render(request, 'quiz/politicsquiz.html', context)

def iq(request):
    context = {
    'questions': IQTest.objects.all()
    }
    return render(request, 'quiz/iqtest.html', context)

def fastfood(request):
    context = {
    'questions': FastFood.objects.all()
    }
    return render(request, 'quiz/fastfood.html', context)