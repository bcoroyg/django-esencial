'''Socialgram views'''

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime

# Una vista en DJANGO es una función
def hello_world(request):
    'Return a greeting.'
    # %b ⇒ Mouth
    # %d ⇒ Day
    # %Y ⇒ Year
    # %H ⇒ Hour
    # %M ⇒ Minute
    # now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))
    )

def hi(request):
    'Hi'
    # import pdb; pdb.set_trace() #LIBRERIA PARA DEBUG
    '''
    request
    request.META
    request.method
    request.GET

    # c ⇒ continua
    '''
    # print(request) # <WSGIRequest: GET '/hi/'>
    param_number = request.GET['numbers'] # parameters /?numbers=1,2,3,4,5
    numbers = param_number.split(',')
    numbers = [int(x) for x in numbers]
    numbers.sort()
    return JsonResponse(numbers, safe=False)