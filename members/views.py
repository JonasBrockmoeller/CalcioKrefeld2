import json
from django.http import HttpResponse, JsonResponse
from members.models import Member


def get_members(request):
    members = Member.objects.all().values()
    print(members)
    return HttpResponse(members)

def new_member(request):
    member_instance = None
    print("request for new member received!")
    try:
        # Use default values if the request body is empty
        if not request.body:
            print("no body problem")
        else:
            data = json.loads(request.body)

            member_id = data.get('appleId')
            member_email = data.get('email')
            member_firstname = data.get('firstname')
            member_lastname = data.get('lastname')

            if member_id not in Member.objects.all().values_list('appleId', flat=True):
                print("adding user")
                member_instance = Member.objects.create(appleId=member_id, email=member_email, firstname=member_firstname, lastname=member_lastname)
            else:
                print("User exists already in DB")


    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return HttpResponse(member_instance)

