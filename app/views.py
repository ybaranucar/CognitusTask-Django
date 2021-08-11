from .models import Data
from .serializers import TaskSerializer

from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.http import Http404
import os
import requests


class CrudView(APIView):
    
    def get(self, request, pk=None, format=None):
        id = pk
        if id == None:
            data_list = Data.objects.all().order_by('-id')
            serializer = TaskSerializer(data_list, many=True)
            return Response(serializer.data)
        
        else:
            try:
                data_detail = Data.objects.get(id=pk)
                serializer = TaskSerializer(data_detail, many=False)
                return Response(serializer.data)
            except Data.DoesNotExist:
                raise Http404("No MyModel matches the given query.")
     
     
    def post(self, request, pk=None, format=None):
        id = pk
        if id == None:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()    
            return Response(serializer.data)
    
        else:
            try:
                data = Data.objects.get(id=pk)
                serializer = TaskSerializer(instance=data, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data)
            except Data.DoesNotExist:
                raise Http404("No MyModel matches the given query.")


    def delete(self, request, pk, format=None):
        try:
            data = Data.objects.get(id=pk)
            data.delete()
            return Response('Item succsesfully delete!')
        except Data.DoesNotExist:
            raise Http404("No MyModel matches the given query.")

class AlgorithmViews(APIView):
    
    def get(self, request, format=None):
        url = os.environ.get('REQUEST_URL')
        r = requests.get(url + '/train/')
        return Response(r.json())
    
    
    def post(self, request, format=None):
        url = os.environ.get('REQUEST_URL')
        r = requests.post(url + '/predict/', data=request.data)
        return Response(r.json())


