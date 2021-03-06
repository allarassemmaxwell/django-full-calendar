from django.shortcuts import render
from .models import *
from django.http import JsonResponse






# LANDING FUNCTION
def home_view(request):
    context  = { }
    template = "index.html"
    return render(request, template, context)









def calendar(request):
    all_events = Events.objects.all()
    context = {"events": all_events,}
    return render(request,'calendar.html',context)








def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                         
    return JsonResponse(out, safe=False)  











def add_event(request):
	print("==== ADD EVENT HERE =====")
	start = request.GET.get("start", None)
	end   = request.GET.get("end", None)
	title = request.GET.get("title", None)
	event = Events(name=str(title), start=start, end=end)
	event.save()
	data  = {}
	return JsonResponse(data)










def update(request):
	start = request.GET.get("start", None)
	end = request.GET.get("end", None)
	title = request.GET.get("title", None)
	id = request.GET.get("id", None)
	event = Events.objects.get(id=id)
	event.start = start
	event.end = end
	event.name = title
	event.save()
	data = {}
	return JsonResponse(data)











def remove(request):
	id = request.GET.get("id", None)
	event = Events.objects.get(id=id)
	event.delete()
	data = {}
	return JsonResponse(data)









def event(request):
    all_events = Events.objects.all()
    # get_event_types = Events.objects.only('event_type')

    # if filters applied then get parameter and filter based on condition else return object
    # if request.GET:  
    #     event_arr = []
    #     if request.GET.get('event_type') == "all":
    #         all_events = Events.objects.all()
    #     else:   
    #         all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))

    #     for i in all_events:
    #         event_sub_arr = {}
    #         event_sub_arr['title'] = i.name
    #         start = datetime.datetime.strptime(str(i.start.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
    #         end = datetime.datetime.strptime(str(i.end.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
    #         event_sub_arr['start'] = start
    #         event_sub_arr['end'] = end
    #         event_arr.append(event_sub_arr)
    #     return HttpResponse(json.dumps(event_arr))

    context = {
        "events": all_events,
        # "get_event_types": get_event_types,
    }
    return render(request,'event.html',context)



