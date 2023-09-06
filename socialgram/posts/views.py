'''Posts views'''

# DJANGO
from django.shortcuts import HttpResponse

# UTILITIES
from datetime import datetime

# Create your views here.
now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
posts = [
    {
        "id":1,
        "name":"Hammad",
        "user":"Fears",
        "timestamp":now,
        "picture":"http://dummyimage.com/231x100.png/5fa2dd/ffffff"
    },
    {
        "id":2,
        "name":"Bendite",
        "user":"Greenhouse",
        "timestamp":now,
        "picture":"http://dummyimage.com/204x100.png/ff4444/ffffff"
    },
    {
        "id":3,
        "name":"Rafaelita",
        "user":"Balma",
        "timestamp":now,
        "picture":"http://dummyimage.com/158x100.png/cc0000/ffffff"
    },
    {
        "id":4,
        "name":"Madelin",
        "user":"Vlasenko",
        "timestamp":now,
        "picture":"http://dummyimage.com/183x100.png/ff4444/ffffff"
    },
    {
        "id":5,
        "name":"Keith",
        "user":"Sergean",
        "timestamp":now,
        "picture":"http://dummyimage.com/151x100.png/cc0000/ffffff"
    },
    {
        "id":6,
        "name":"Gilligan",
        "user":"Burchett",
        "timestamp":now,
        "picture":"http://dummyimage.com/163x100.png/5fa2dd/ffffff"
    },
    {
        "id":7,
        "name":"Tracey",
        "user":"Bevir",
        "timestamp":now,
        "picture":"http://dummyimage.com/208x100.png/dddddd/000000"
    },
    {
        "id":8,
        "name":"Fidela",
        "user":"Krystof",
        "timestamp":now,
        "picture":"http://dummyimage.com/163x100.png/ff4444/ffffff"
    },
    {
        "id":9,
        "name":"Bree",
        "user":"Sculpher",
        "timestamp":now,
        "picture":"http://dummyimage.com/107x100.png/cc0000/ffffff"
    },
    {
        "id":10,
        "name":"Viviene",
        "user":"Lowry",
        "timestamp":now,
        "picture":"http://dummyimage.com/229x100.png/dddddd/000000"
    }
]


def list_posts(request):
    '''List existing posts'''
    content = []
    for post in posts:
        content.append('''
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        '''.format(**post))
    return HttpResponse('<br>'.join(content))