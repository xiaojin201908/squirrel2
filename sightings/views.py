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
    context = dict()
    if request.method == 'POST':
            s = Squirrel()
            s.longitude = request.POST.get('longitude')
            s.latitude = request.POST.get('latitude')
            temp_id = request.POST.get('unique_squirrel_id')
            while temp_id in Squirrel.objects.values_list('unique_squirrel_id',flat=True):
                temp_id  += '-R'
            s.unique_squirrel_id = temp_id
            s.shift = request.POST.get('shift')
            s.date = datetime.datetime.strptime(request.POST.get('date'),'%Y-%m-%d')
            date_error = None
            if s.date > datetime.datetime.now():
                date_error = 'Date automatically corrected to today!'
                s.date = datetime.datetime.now().date()
            s.age = request.POST.get('age')
            s.primary_fur_color = request.POST.get('primary_fur_color')
            s.location = request.POST.get('location')
            s.specific_location = request.POST.get('specific_location')
            s.running = request.POST.get('running')
            s.chasing = request.POST.get('chasing')
            s.climbing = request.POST.get('climbing')
            s.eating = request.POST.get('eating')
            s.foraging = request.POST.get('foraging')
            s.other_activities = request.POST.get('other_activities')
            s.kuks = request.POST.get('kuks')
            s.quaas = request.POST.get('quaas')
            s.moans = request.POST.get('moans')
            s.tail_flags = request.POST.get('tail_flags')
            s.tail_twitches = request.POST.get('tail_twitches')
            s.approaches = request.POST.get('approaches')
            s.indifferent = request.POST.get('indifferent')
            s.runs_from = request.POST.get('runs_from')
            s.save()
            yes = 'Successfully added!'
            
            context = {'date_error':date_error,
                       'success':yes,}
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
    
    # fur color
    color_list = [value[0] for value in list(Squirrel.objects.all().values_list('primary_fur_color'))]
    color_dict = dict(Counter(color_list))
    color_dict.pop('')

    # shift
    shift_list = [value[0] for value in list(Squirrel.objects.all().values_list('shift'))]
    shift_dict = dict(Counter(shift_list))

    # response
    approaches_count = len([value[0] for value in list(Squirrel.objects.all().values_list('approaches')) if value[0] == 'true'])
    indifferent_count = len([value[0] for value in list(Squirrel.objects.all().values_list('indifferent')) if value[0] == 'true'])
    runs_from_count = len([value[0] for value in list(Squirrel.objects.all().values_list('runs_from')) if value[0] == 'true'])
    response_dict = {'Approaches':approaches_count,
            'Indifferent':indifferent_count,
            'Runs From': runs_from_count,}

    # tails
    tail_flag_count = len([value[0] for value in list(Squirrel.objects.all().values_list('tail_flags')) if value[0] == 'true'])
    tail_twitch_count = len([value[0] for value in list(Squirrel.objects.all().values_list('tail_twitches')) if value[0] == 'true'])
    tail_dict = {'Flags':tail_flag_count,
                     'Twitches':tail_twitch_count,}
    
    context = {'adult_juvenile': adult_juvenile,
               'color_dict': color_dict,
               'shift_dict': shift_dict,
               'response_dict': response_dict,
               'tail_dict':tail_dict,}
   
    return render(request,'sightings/stats.html',context)


def map_plot(request):
    n = 100
    lats = Squirrel.objects.values_list('latitude',flat=True)[:n]
    longs = Squirrel.objects.values_list('longitude',flat=True)[:n]
    ids = Squirrel.objects.values_list('unique_squirrel_id',flat=True)[:n]

    geo_json = [ {"type": "Feature",
                        "properties": {
                            "id":  ident,
                            "popupContent":  "squirrel_id=%s" % (ident,) 
                            },
                        "geometry": {
                            "type": "Point",
                            "coordinates": [float(lon),float(lat)] }}
                        for ident,lon,lat in zip(ids,longs,lats) ] 
    context = {'geo_json':geo_json}

    return render(request, 'sightings/map.html', context)
