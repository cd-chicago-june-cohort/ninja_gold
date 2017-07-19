# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from random import randint

from time import gmtime, strftime


#-----------------------------------------------------------------
#-----------------------------------------------------------------


def index(request):
    
    if 'score' not in request.session:
        request.session['score'] = 0
    if 'messages' not in request.session:
        request.session['messages'] = []

    return render(request, 'ninja/index.html')


#-----------------------------------------------------------------
#-----------------------------------------------------------------


def process_money(request):
    
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    
    if request.POST["building"] == "farm":
        farm_rand = randint(10, 20)
        request.session["score"] += farm_rand
        request.session["messages"].append("Earned " + str(farm_rand) + " golds at the farm!  -at " + time)
    elif request.POST["building"] == "cave":
        cave_rand = randint(5,10)
        request.session["score"] += cave_rand
        request.session["messages"].append("Earned " + str(cave_rand) + " golds at the cave!  -at " + time)
    elif request.POST["building"] == "house":
        house_rand = randint(2, 5)
        request.session["score"] += house_rand
        request.session["messages"].append("Earned " + str(house_rand) + " golds at the house!  -at " + time)
    elif request.POST["building"] == "casino":
        casino_rand = randint(-50, 50)
        request.session["score"] += casino_rand
        request.session['messages'].append("Earned " + str(casino_rand) + " golds at the casino!  -at " + time)
        
    return redirect('/')


#-----------------------------------------------------------------
#-----------------------------------------------------------------

def clear_session(request):
    request.session['score'] = 0
    request.session['messages'] = []
    return redirect('/')


