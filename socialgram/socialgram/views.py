'''Socialgram views'''

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime
from json import dumps

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

def sort_num(request):
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
    # param_number = request.GET['numbers'] # parameters /?numbers=1,2,3,4,5
    # numbers = param_number.split(',')
    
    # LIST CONVERGETIONS [int(x) for x in numbers]
    numbers = [int(x) for x in request.GET['numbers'].split(',')]
    # numbers.sort()
    sorted_numbers = sorted(numbers)

    data = {
        'status': 'success',
        'numbers': sorted_numbers,
        'message': 'Integer sorted successfully!'
    }
    # return JsonResponse(numbers, safe=False)
    # return HttpResponse(str(order), content_type='application/json')
    return HttpResponse(dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Socialgram'.format(name)
    return HttpResponse(message)