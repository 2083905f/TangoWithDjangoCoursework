from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': "I am bold from the context"}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page <br/> <a href='/rango/'>index</a>"
                        "<br/> This has been put together by Kelvin Fowler, 2083905")


