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
>>> from geopy import distance 
>>> wellington = (-41.32, 174.81)
>>> salamanca = (40.96, -5.50)
>>> print(distance.distance(wellington, salamanca).km)
19959.6792674
'''


'''
from datetime import datetime
from django.shortcuts import render


def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })
'''