from django.http import JsonResponse
from db import query_lines, query_stations

def lines_view(request):
    return JsonResponse(query_lines(), safe=False)


def stations_view(request):
    return JsonResponse(query_stations(), safe=False)