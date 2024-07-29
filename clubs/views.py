from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse

from clubs.models import Club


def getClubs(request):
    data = Club.objects.values()
    return JsonResponse(list(data), safe=False)