from django.shortcuts import render , redirect
from .models import *
from django.views import View
from .serializor import OutageModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def login(request):
    pass

import datetime
def convert(date_time):
    format = '%Y-%m-%d %H:%M:%S' # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
    return datetime_str

class OutageAPITracker(APIView):
    def post(self,request):
        try:
            count = OutageModel.objects.all().count()
            if count > 20:
               return Response({"error":"Not able to Create More"},status=status.HTTP_400_BAD_REQUEST) 
            data = {
                "received_from":request.data['received_from'],
                "application_name":request.data['application_name'],
                "outage_start_time":convert(request.data['outage_start_time']),
            }
            Outage = OutageModel.objects.create(**data)
            query_data = OutageModelSerializer(OutageModel.objects.all().order_by('-create_date'), many=True)
            return Response(query_data.data)
        except Exception as e:
            print(e)
            return Response({"error":"Unable to Create"},status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        try:
            query_set = OutageModel.objects.filter(pk=pk)
            data = OutageModelSerializer(query_set,many=True).data[0]
            return Response(data)
        except Exception as e:
            print(e)
            return Response({"error":"Unable to Update"},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            print(request.data)
            query_set = OutageModel.objects.filter(pk=pk)
            query_set.update(outage_end_time=request.data['outage_end_time'])
            min = (query_set.first().outage_end_time - query_set.first().outage_start_time).total_seconds()/60
            query_set.update(outage_status=True,outage_time=int(min))
            data = OutageModelSerializer(OutageModel.objects.all().order_by('-create_date'),many=True).data
            return Response(data)
        except Exception as e:
            print(e)
            return Response({"error":"Unable to Update"},status=status.HTTP_400_BAD_REQUEST)

class OutageTracker(View):
    def get(self,request):
        context = {}
        try:
            context['outage'] =OutageModel.objects.all().order_by('-create_date')
        except Exception as e:
            print(e)
        
        return render(request,'outage.html',context)

