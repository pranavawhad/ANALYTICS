from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseServerError
from django.utils.dateparse import parse_datetime



@api_view(['POST'])
def website(request):
    if request.method =='POST':
        data = request.data 
        ip = data.get('userIPAddress')
        
        instance, created = WebInfo.objects.get_or_create(userIPAddress=ip)
        
        if created:
            instance.Website = data.get('website')
            instance.save()
            return Response({'data': 'Created'}, status=201)
        else:
            return Response({'error': 'Already exists'})

    return Response({'data': 'Not Received'}, status=400)
    
@api_view(['POST'])        
def entry(request):
    if request.method == 'POST':
        data = request.data
        entrydata  = data.get('entryInfo',[])
        userip = data.get('userIPAddress')
        
        infoinstance = WebInfo.objects.get(userIPAddress = userip)
        
        for entry in entrydata:
            pagename = entry['page']
            Time = entry['accessTime']
            
            Entry.objects.create(Page=pagename,AccessTime=Time,userIPAddress=infoinstance)
    return Response('success')
            
            
            
@api_view(['POST'])
def hover(request):
    if request.method =='POST':
        data = request.data 
        hoverdata = data.get('hover',[])
        userip = data.get('userIPAddress')
        info = WebInfo.objects.get(userIPAddress = userip)
        
        for entry in hoverdata:
            x = entry['x']
            y= entry['y']
            page = entry['page']
            Time = entry['time']
            type = entry['event-type']
            loc = entry['place_of_hover']
            inf = entry['attributes']
            
            Hover.objects.create(X=x,Y=y,page=page,Time=Time,type=type,Location=loc,Information=inf,userIPAddress=info)
        
        
    return Response('sucesss')
        
        
@api_view(['POST'])
def click(request):
    if request.method=='POST':
        data = request.data
        clickdata = data.get('click',[])
        userip = data.get('userIPAddress')
        info = WebInfo.objects.get(userIPAddress = userip)
        for entry in clickdata:
            x = entry['x']
            y = entry['y']
            page = entry['page']
            time = entry['time']
            event = entry['event-type']
            place = entry['place_of_click'] 
            
            Click.objects.create(XC=x,YC=y,pageC=page,TimeC=time,typeC=event,LocationC=place,userIPAddress=info)
            
        
    return Response('success')

        
        
@api_view(['POST'])
def app(request):
    if request.method =='POST':
        data = request.data 
        u = data.get('userIPAddress')
        i = WebInfo.objects.get(userIPAddress = u)
        
        Pages.objects.create(
            First_Page = data.get('first_page'),
            Other_Pages = ','.join(data.get('other_pages',[])),
            FirstPageAccessTime = parse_datetime(data.get('time')),
            userIPAddress = i
            
            
        )
        
    return Response('success')
        
    
def tophover(request):
    unique = WebInfo.objects.values_list('userIPAddress',flat=True).distinct()
    hoverhistory = []
    
    for userip in unique:
        h_for_user = Hover.objects.filter(userIPAddress__userIPAddress=userip).order_by('-Time')[:10]
        hoverhistory.append({'userip':userip,'hoverdata':h_for_user})
        
    context = {'hoverhistory':hoverhistory}
    return render(request,'hover.html',context)

def topclick(request):
    unique = WebInfo.objects.values_list('userIPAddress',flat=True).distinct()
    clickhistory = []
    
    for userip in unique:
        c_for_user = Click.objects.filter(userIPAddress__userIPAddress=userip).order_by('-TimeC')[:10]
        clickhistory.append({'userip':userip,'clickdata':c_for_user})
        
    context = {'clickhistory':clickhistory}
    return render(request,'click.html',context)

def user(request):
    all = WebInfo.objects.all()
    user_data = []
    for user in all:
        v = Pages.objects.filter(userIPAddress=user).order_by('FirstPageAccessTime')
        user_data.append({'info':user,'visited':v})
    context = {'user_data':user_data}
    return render(request,'info.html',context)

def time(request):
    userip = WebInfo.objects.values_list('userIPAddress',flat=True).distinct()
    a = []
    for i in userip:
        info = WebInfo.objects.get(userIPAddress = i)
        p = Entry.objects.filter(userIPAddress = info).order_by('AccessTime')[:10]
        a.append({'info':info,'p':p})
        
    context = {'a':a}
    return render(request,'time.html',context)
