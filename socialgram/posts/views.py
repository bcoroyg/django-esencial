'''Posts views'''

# DJANGO
# from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# UTILITIES
from datetime import datetime

# Create your views here.
now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
posts = [
    {
        "id":1,
        "title":"Hammad",
        "user": { 
            "name":"Fears",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/231/300/300"
    },
    {
        "id":2,
        "title":"Bendite",
        "user": { 
            "name":"Greenhouse",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/232/300/300"
    },
    {
        "id":3,
        "title":"Rafaelita",
        "user": { 
            "name":"Balma",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/233/300/300"
    },
    {
        "id":4,
        "title":"Madelin",
        "user": { 
            "name":"Vlasenko",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/234/300/300"
    },
    {
        "id":5,
        "title":"Keith",
        "user": { 
            "name":"Sergean",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/235/300/300"
    },
    {
        "id":6,
        "title":"Gilligan",
        "user": { 
            "name":"Burchett",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/236/300/300"
    },
    {
        "id":7,
        "title":"Tracey",
        "user": { 
            "name":"Bevir",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/237/300/300"
    },
    {
        "id":8,
        "title":"Fidela",
        "user": { 
            "name":"Krystof",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/238/300/300"
    },
    {
        "id":9,
        "title":"Bree",
        "user": { 
            "name":"Sculpher",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/239/300/300"
    },
    {
        "id":10,
        "title":"Viviene",
        "user": { 
            "name":"Lowry",
            "picture":"https://loremflickr.com/g/50/50/boy/all"
        },
        "timestamp":now,
        "photo":"https://picsum.photos/id/240/300/300"
    }
]

@login_required
def list_posts(request):
    '''List existing posts'''
    """ content = []
    for post in posts:
        content.append('''
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        '''.format(**post))
    return HttpResponse('<br>'.join(content)) """
    return render(request, 'posts/feed.html', {'posts':posts})