from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView, api_view, action
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import *
from .serializer import *
from rest_framework import status
from ipware import get_client_ip


class WorksView(ListCreateAPIView):
    queryset = Works.objects.all()
    serializer_class = WorkSerializer

class WorksGETbyID(APIView):

    def get(self, request, pk):
        work = Works.objects.get(id=pk)
        client_ip, is_routable = get_client_ip(request) 
        if client_ip is None:
            # Unable to get the client's IP address
            return Response('fuck')
        else:
            # We got the client's IP address
            work.views += 1
            work.save()
            ser = WorkSerializer(work, many=False)
            return Response(ser.data) 


class WorkTrue(ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorkSerializer

    def list(self, request):
        work = Works.objects.all()
        a = []
        for i in work:
            if i.finished == True:
                dat = {
                    'Name': i.name,
                    'Day': i.day,
                    'Finished': i.finished,
                }
                a.append(dat)
                data = {
                    "These works are finished ":
                    a
                }
        return Response(data)


class WorkFalse(ListAPIView):
    queryset = Works.objects.all()
    serializer_class = WorkSerializer

    def list(self, request):
        work = Works.objects.all()
        a = []
        for i in work:
            if i.finished == False:
                dat = {
                    'Name': i.name,
                    'Day': i.day,
                    'Not Finished': i.finished,
                }
                a.append(dat)
                data = {
                    "These works are not finished yet":
                    a
                }
        return Response(data)
        