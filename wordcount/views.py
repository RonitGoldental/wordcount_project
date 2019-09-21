from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter

def home(request):
    return render(request,'home.html')


def eggs(request):
    return HttpResponse('eggs')


def count(request):
    fulltext= request.GET['fulltext']
    word_list=fulltext.split()
    counter_of_words=Counter(word_list)
    return render(request, 'count.html',{'fulltext':fulltext, 'number':len(word_list),'counter_of_words':counter_of_words})


def about(request):
    return render(request, 'about.html')