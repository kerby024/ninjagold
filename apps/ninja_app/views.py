# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
    if 'yourgold' and 'youractivities' in request.session:
        pass
    else:
        request.session['yourgold'] = 0
        request.session['youractivities']=[]
    return render(request, 'ninja_app/index.html')

def processmoney(request):
    if request.method =='POST':
        if request.POST['building'] == 'farm':
            farmMoney = random.randrange(10,21)
            request.session['yourgold']  += farmMoney
            now = datetime.datetime.now()
            myStr = "Earned " + str(farmMoney) + " gold from the farm " + str(now)
            request.session['youractivities'].append(myStr)
        elif request.POST['building'] == 'cave':
            caveMoney = random.randrange(5,11)
            request.session['yourgold'] += caveMoney
            now = datetime.datetime.now()
            myStr = "Earned " + str(caveMoney) + " gold from the cave " + str(now)
            request.session['youractivities'].append(myStr)
        elif request.POST['building'] == 'house':
            houseMoney = random.randrange(2,6)
            request.session['yourgold'] += houseMoney
            now = datetime.datetime.now()
            myStr = "Earned " + str(houseMoney) + " gold from the house " + str(now)
            request.session['youractivities'].append(myStr)
        elif request.POST['building'] == 'casino':
            casinoMoney = random.randrange(-50,51)
            request.session['yourgold'] += casinoMoney
            now = datetime.datetime.now()
            myStr = "Entered a casino and earned " + str(casinoMoney) + " " + str(now)
            request.session['youractivities'].append(myStr)
   
        return redirect('/')

# def confirm(request):
#     return render(request, 'ninja_app/confirm.html', {'total': request.session['total']})

# def clear(request):
#     request.session.flush()
#     return redirect ('/')

# Create your views here.
