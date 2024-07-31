import json

from django.http import JsonResponse, HttpResponse

from prognosis.models import Prognosis


# Create your views here.
def get_latest_prognosis(request):
    try:
        # Use default values if the request body is empty
        if not request.body:
            print("no body problem")
        else:
            data = json.loads(request.body)
            member_id = data.get('appleId')
            result = Prognosis.objects.filter(created_by=member_id).order_by('created_on').values().first()
            print(result)
            return HttpResponse(result)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def new_prognosis(request):
    prognosis_instance = None
    print("request for new prognosis received!")
    try:
        # Use default values if the request body is empty
        if not request.body:
            print("no body problem")
        else:
            data = json.loads(request.body)

            print("adding result")
            prognosis_instance = Prognosis.objects.create(created_by = data.get('appleId'),
                                                            created_on = data.get('created_on'),
                                                            prognosis_champion = data.get('prognosis_champion'),
                                                            prognosis_topscorer =  data.get('prognosis_topscorer'),
                                                            prognosis_trainer_fired =  data.get('prognosis_trainer_fired'),
                                                            prognosis_surprise = data.get('prognosis_surprise'),
                                                            prognosis_disappointment = data.get('prognosis_disappointment'),
                                                            prognosis_hottake = data.get('prognosis_hottake')
                                                            )
            return HttpResponse(prognosis_instance)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)