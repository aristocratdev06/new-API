from django.shortcuts import render
from .serializers import *
from .models import Krosovka
#rest_framework
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
def home(request):
    return render(request, "home.html")

# APi to'liq chaqrish
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def krasovkaMakeApi(request):
    krasovka = Krosovka.objects.all()
    serializer = KrsaovkaAPI(krasovka, many=True) 
    return Response(serializer.data)

# API id orqali topish
@api_view(["GET"])
@permission_classes((permissions.AllowAny, ))
def singleapi(request, pk):
    krasovka = Krosovka.objects.get(id=pk)
    serializer = KrsaovkaAPI(krasovka, many=False)
    return Response(serializer.data)

# API post joylash

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def PostJoylash(request):
    serializer = KrsaovkaAPI(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def PostYangilash(request, pk):
    krasovka = Krosovka.objects.get(id=pk)
    serializer = KrsaovkaAPI(instance=krasovka, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def PostDelete(request, pk):
    krasovka = Krosovka.objects.get(id=pk)
    krasovka.delete()
    return Response("o'chirdingiz")
