from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .models import Metar
from .serializers import MetarSerializer



def ping(request):
    return JsonResponse({'data':'pong'})



def get_data(filter_station):
    """Fetch data from DB"""
    print("Data comming from DB")
    data = Metar.objects.filter(station=filter_station).order_by('-last_observation').first()
    return data
    
    


def latestData(request):
    
    filter_station = request.GET.get('scode')
    nocache = request.GET.get("nocache")
    
    if filter_station:
        """ Fetch data """     
        if(nocache=="1"):
            """ Refresh Cache and Fetch data from db"""
            cache.clear()
            message="Cache Has been cleared, Data is comming from DB"
            latestData = get_data(filter_station)
            
        else:    
            """Fetch data from Cache"""
            if cache.get(filter_station):
                print("Data comming From Cache")
                message = "Data Coming from Cache"
                latestData = cache.get(filter_station)

            else:
                """ Fetch data from db and set into Cache"""
                message = "Data Coming from DB"
                latestData = get_data(filter_station)
                cache.set(filter_station, latestData,timeout = 300)           
            
        serializer = MetarSerializer(latestData,many=False)
        context ={'data':serializer.data,'message':message}

        return render(request,"api/home.html",context)

    context = {"message":"No Data Fetched. Please try to search right keyword"}

    return render(request,"api/home.html",context)

