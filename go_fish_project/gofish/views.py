from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import json
from generators import *

from gofish.forms import PlayerForm, UserForm
from gofish.models import Bait, Boat, OwnsBait, Player

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
    
def register(request):
    context = RequestContext(request)
    registered = False
    
    # If submitting forms
    if request.method == 'POST':
        
        # Attempt to get data from raw forms
        user_form = UserForm(data=request.POST)
        player_form = PlayerForm(data=request.POST)
        
        # Valid forms -> save data
        if user_form.is_valid() and player_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            player = player_form.save(commit=False)
            player.user = user
            player.save()
            
            registered = True
            
        else:
            print user_form.errors, player_form.errors
    
    # If accessing page to register an account
    else:
        user_form = UserForm()
        player_form = PlayerForm()
        
    return render_to_response(
            'gofish/register.html',
            {'user_form': user_form, 'player_form': player_form, 'registered': registered},
            context)
    
def user_login(request):
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/gofish/')
            else:
                return HttpResponse("Your Go!Fish account is disabled.")
        else:
            # Bad login details were provided.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        return render_to_response('gofish/login.html', {}, context)
            
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/gofish/')

def rankings(request):
    context = RequestContext(request)
    
    player_list = Player.objects.order_by('-money')[:10]
    context_dict = {'top10players': player_list}
    return render_to_response('gofish/rankings.html', context_dict, context)

@login_required
def game(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/game.html', context_dict, context)

@login_required
def shop(request):
    context = RequestContext(request)
    # Get current player
    current_player = Player.objects.get(user=request.user)
    
    boat_list = Boat.objects.order_by('price')
    bait_list = Bait.objects.order_by('price')
    # Get owned bait of current player
    owned_bait = OwnsBait.objects.filter(
            # Link to current player
            player=current_player
            
        ).filter(
            # Only interested in currently available bait
            amount__gt=0
        )
    context_dict = {'player': current_player, 'boats': boat_list, 'bait': bait_list, 'owned_bait': owned_bait}
    return render_to_response('gofish/shop.html', context_dict, context)

@login_required
def trophies(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('gofish/trophies.html', context_dict, context)

### API calls, return json ###
def newgame(request):
    res = {'lake': generateLake(), 'weather': {}, 'currentTime': 6, 'money': 100}
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