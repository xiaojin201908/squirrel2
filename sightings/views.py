from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import Squirrel
from .forms import SquirrelForm
import datetime

def all_list(request):
    all_squirrel = Squirrel.objects.all()[::-1]
    return render(request, 'sightings/all_list.html',{'all_squirrels':all_squirrel})
    
def add(request):
    if request.method =='POST':
        form = SquirrelForm(request.POST)
        #check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/sighting/all_list')
        
        else:
            context= {'form': form,
                      'error': 'The form was not valid. Please do it again.'}

            return render(request,'sightings/edit.html' , context) 
    else:
        form = SquirrelForm()
    context = {
            'form':form,
    }
    return render(request,'sightings/add.html',context)


def update(request,unique_squirrel_id):
    upup = Squirrel.objects.get(unique_squirrel_id=unique_squirrel_id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance=upup)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    
        else:
            context= {'form': form,
                      'error': 'The form was not valid. Please do it again.'}

            return render(request,'sightings/edit.html' , context)      

    else:
        form = SquirrelForm(instance=upup)
        context = {'form': form,
                  'instance': upup}

        return render(request, 'sightings/edit.html', context)


def stats(request):
    from collections import Counter
    # number of adults per juvenile
    age_list = [value[0] for value in list(Squirrel.objects.all().values_list('age'))]
    age_dict = dict(Counter(age_list))
    adult_juvenile = age_dict['Adult']/age_dict['Juvenile']
    adult_juvenile = round(adult_juvenile,2)
    
    # Running
    run_list = [value[0] for value in list(Squirrel.objects.all().values_list('running'))]
    run_dict = dict(Counter(run_list))
   

    # shift
    shift_list = [value[0] for value in list(Squirrel.objects.all().values_list('shift'))]
    shift_dict = dict(Counter(shift_list))

    #eating
    eat_list = [value[0] for value in list(Squirrel.objects.all().values_list('eating'))]
    eat_dict = dict(Counter(eat_list))
    
    #Climbing
    climb_list = [value[0] for value in list(Squirrel.objects.all().values_list('climbing'))]
    climb_dict = dict(Counter(climb_list))  
   

    return render(request,'sightings/stats.html',context)


def map_plot(request):
    n = 100
    lats = Squirrel.objects.values_list('latitude',flat=True)[:n]
    longs = Squirrel.objects.values_list('longitude',flat=True)[:n]
    ids = Squirrel.objects.values_list('unique_squirrel_id',flat=True)[:n]

    mapmap = [ {"type": "Feature",
                        "properties": {
                            "id":  ident,
                            "popupContent":  "squirrel_id=%s" % (ident,) 
                            },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [float(lon),float(lat)] }}
                        for ident,lon,lat in zip(ids,longs,lats) ] 
    context = {'geo_json':mapmap}

    return render(request, 'sightings/map.html', context)
