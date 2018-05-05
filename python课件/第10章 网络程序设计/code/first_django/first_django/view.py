from django.http import HttpResponse

def hello(request):
    return HttpResponse('This is my first django application!')

def greeting(request):
    return HttpResponse('Hello everyone!')
