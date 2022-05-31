from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from tea_app.models import Colors, Teas
from tea_app.serializers  import ColorSerializer, TeaSerializer
from django.shortcuts import render, get_object_or_404

from rest_framework.parsers import JSONParser
from rest_framework import status, viewsets
from rest_framework.response import Response

# Create your views here.
def index(request):
    http = \
    """
    <html lang="ru">
    <head>
        <title>Веб-сервер</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></meta>
        <h1>Hello from Django!</h1>
    </head>
    <body>
        <h4>Here you can learn more about tea.</h1>
        <ul>
            <li>/restapi/tea/</li>
            <li>/restapi/color/</li>
        </ul>
    </html>
    """
    return HttpResponse(http)

class ColorViewSet(viewsets.ModelViewSet):
    queryset = Colors.objects.all()
    serializer_class = ColorSerializer

class TeaViewSet(viewsets.ModelViewSet):
    queryset = Teas.objects.all()
    serializer_class = TeaSerializer

