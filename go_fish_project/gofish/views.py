from django.template import RequestContext
from django.shortcuts import render_to_response

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
    return render_to_response('gofish/logn.html', context_dict, context)
    
def register(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/register.html', context_dict, context)
    
def game(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/game.html', context_dict, context)