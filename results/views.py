import json
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from results.models import Result

def get_results(request):
    results = Result.objects.all().values()
    print(results)
    return HttpResponse(results)


# Create your views here.
def get_latest_homeranking_result(request):
    try:
        # Use default values if the request body is empty
        if not request.body:
            print("no body problem")
        else:
            data = json.loads(request.body)
            member_id = data.get('appleId')
            results = Result.objects.filter(created_by=member_id).order_by('created_on')
            # Convert QuerySet to a list of dictionaries
            result_list = list(results.values())
            return JsonResponse(result_list, safe=False)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def new_result(request):
    result_instance = None
    print("Request for new result received!")
    try:
        # Use default values if the request body is empty
        if not request.body:
            print("No body problem")
        else:
            data = json.loads(request.body)
            print("Adding result")
            result_instance = Result.objects.create(
                created_by=data.get('appleId'),
                created_on=datetime.now(),
                homeranking=data.get('homeranking'),
                awayranking=data.get('awayranking'),
                logoranking=data.get('logoranking')
            )
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    result_dict = {
        'id': result_instance.id,
        'created_by': result_instance.created_by,
        'created_on': result_instance.created_on,
        'homeranking': result_instance.homeranking,
        'awayranking': result_instance.awayranking,
        'logoranking': result_instance.logoranking
    }

    return JsonResponse(result_dict)
