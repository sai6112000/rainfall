from multiprocessing import context
from django.shortcuts import render, HttpResponse

from min_max import avg_t, loc_yr, location, year



def index(request):
    context={
        'variable':'this is shetty yo'
    }
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("this is a about page")

def contact(request):
    return HttpResponse("this is a contact page")

def services(request):
    return HttpResponse("this is a services page")

def search(request):
    return render(request,'home.html')


def search_res(request):
    mintemp=int(request.POST.get("mintemp"))
    maxtemp=int(request.POST.get("maxtemp"))
    rainfall=int(request.POST.get("rainfall"))
    wgs=int(request.POST.get("wgs"))
    ws9am=int(request.POST.get("ws9am"))
    ws3pm=int(request.POST.get("ws3pm"))
    hum9am=int(request.POST.get("hum9am"))
    hum3pm=int(request.POST.get("hum3pm"))
    pre9am=int(request.POST.get("pre9am"))
    pre3pm=int(request.POST.get("pre3pm"))
    Cloud9am=int(request.POST.get("Cloud9am"))
    Cloud3pm=int(request.POST.get("Cloud3pm"))
    Temp9am=int(request.POST.get("Temp9am"))
    Temp3pm=int(request.POST.get("Temp3pm"))
    location=int(request.POST.get("location"))
    winddir9am=int(request.POST.get("winddir9am"))
    winddir3pm=int(request.POST.get("winddir3pm"))
    windgustdir=int(request.POST.get("windgustdir"))
    raintoday=int(request.POST.get("raintoday"))

    

    import pickle
    import numpy as np
    model=pickle.load(open('xgb.pkl','rb'))
    input_q=np.array([[-1.53166617, 0.19132753 ,-0.04135977 ,-0.20358073  ,1.04522847  ,0.32773639,1.32876628 , 1.36645776 , 0.67781938 , 0.62329359 , 0.08140881 ,-1.44365196, -1.45721533 ,-1.2245635  , 0.99547851 , 0.60794072 ,-0.01407077 , 0.02310362 , -0.52979545]])
    result=model.predict(input_q)[0]
    print(result)
    input_q=np.array([[location, mintemp , maxtemp ,rainfall,windgustdir,wgs,winddir9am , winddir3pm , ws9am , ws3pm , hum9am ,hum3pm, pre9am ,pre3pm  , Cloud9am , Cloud3pm ,Temp9am , Temp3pm , raintoday]])
    print(input_q)
    result=model.predict(input_q)[0]
    print(result)

    result=int(result)
    if result==0:
        result="It will not rain"
    else:
        result="It will rain"
    

    context={
        'variable':result
    }
    return render(request,'home.html',context)


def filter(request):
    return render(request,'filter.html')


def filter_res(request):
    loca=int(request.POST.get("location"))
    yr=int(request.POST.get("year"))
    filter=int(request.POST.get("filter"))
    
    
    if(filter==0):
        v=location(loca)
    elif(filter==1):
        v=year(yr)
    else:
        v=loc_yr(loca,yr)
    
    v=list(v)
    
    if v[5]==0:
        v[5]="E"
    if v[5]==1:
        v[5]="ENE"
    if v[5]==2:
        v[5]="ESE"
    if v[5]==3:
        v[5]="N"
    if v[5]==4:
        v[5]="NE"
    if v[5]==5:
        v[5]="NNE"
    if v[5]==6:
        v[5]="NNW"
    if v[5]==7:
        v[5]="NW"
    if v[5]==8:
        v[5]="S"
    if v[5]==9:
        v[5]="SE"
    if v[5]==10:
        v[5]="SSE"
    if v[5]==11:
        v[5]="SSW"
    if v[5]==12:
        v[5]="SW"
    if v[5]==13:
        v[5]="W"
    if v[5]==14:
        v[5]="WNW"
    if v[5]==15:
        v[5]="WSW"
    

    
    
    context={
        'Min_Temp':v[0],
        'Max_Temp':v[1],
        'Min_Rainfall':v[2],
        'Max_Rainfall':v[3],
        'avg_temp':v[4],
        'avg_WindGustDir':v[5],
        'avg_WindGustSpeed':v[6],
        'avg_humidity_morn':v[7],
        'avg_humidity_aft':v[8],
        'avg_pressure_morn':v[9],
        'avg_pressure_aft':v[10]
    }
    return render(request,'filter.html',context)

def charts(request):
    return render(request,'charts.html')

def charts_res(request):
    
    loca=int(request.POST.get("location"))
    print(loca)
    yr=int(request.POST.get("year"))
    print(yr)
    v=avg_t(loca,yr)
    print(v)
    context={
        't2008':v[0],
        't2009':v[1],
        't2010':v[2],
        't2011':v[3],
        't2012':v[4],
        't2013':v[5],
        't2014':v[6],
        't2015':v[7],
        't2016':v[8],
        't2017':v[9],
        'loc':v[10]
    }
    return render(request,'charts.html',context)