from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('gofish/index.html', context_dict, context)
    
def login(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/login.html', context_dict, context)
    
def register(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/register.html', context_dict, context)
    
def game(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/game.html', context_dict, context)

def shop(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/shop.html', context_dict, context)

def rankings(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/rankings.html', context_dict, context)

def trophies(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/trophies.html', context_dict, context)

### API calls, return json ###
def newgame(request):
    res = {'lake': {}, 'weather': {}, 'currentTime': 6, 'money': 100}
    return HttpResponse(json.dumps(res), content_type="application/json")

def move(request):
    res = {'currentTime': 10}
    return HttpResponse(json.dumps(res), content_type="application/json")

def fish(request):
    res = {'catch': [], 'currentTime': 11}
    return HttpResponse(json.dumps(res), content_type="application/json")

def changebait(request):
    res = {}
    return HttpResponse(json.dumps(res), content_type="application/json")

def buybait(request):
    res = {'money': 97}
    return HttpResponse(json.dumps(res), content_type="application/json")

def buyboat(request):
    res = {'money': 90}
    return HttpResponse(json.dumps(res), content_type="application/json")

def finish(request):
    res = {'money': 110, 'trophies': []}
    return HttpResponse(json.dumps(res), content_type="application/json")
