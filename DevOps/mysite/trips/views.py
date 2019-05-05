from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

def hello_world(request):
    #return HttpResponse("Hello World!")
    # return render(request, 'hello_world.html', {"current_time": str(datetime.now())})
    listdata = "Hello World!"
    return JsonResponse(listdata,safe=False)








'''
from datetime import datetime
from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
    '''