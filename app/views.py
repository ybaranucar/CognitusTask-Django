from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
import requests
from rest_framework import status
from .models import Data
from .serializers import TaskSerializer


@api_view(['GET'])
def url_list(request):
    api_urls = {
        'List':'/data/',
        'Detail':'/data-detail/<str:pk>',
        'Create':'/data-create/',
        'Update':'/data-update/<str:pk>',
        'Delete':'/data-delete/<str:pk>',
    }
    
    return Response(api_urls)


@api_view(['GET'])
def get_data_list(request):
	data_list = Data.objects.all().order_by('-id')
	serializer = TaskSerializer(data_list, many=True)
	return Response(serializer.data)


@api_view(['GET'])
def get_data_detail(request, pk):
	data_detail = Data.objects.get(id=pk)
	serializer = TaskSerializer(data_detail, many=False)
	return Response(serializer.data)
    
    
@api_view(['POST'])
def data_create(request):
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
	    serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def data_update(request, pk):
    data = Data.objects.get(id=pk)
    serializer = TaskSerializer(instance=data, data=request.data)

    if serializer.is_valid():
    	serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def data_delete(request, pk):
	data = Data.objects.get(id=pk)
	data.delete()

	return Response('Item succsesfully delete!')


@api_view(['GET'])
def get_train(request):
    r = requests.get('http://127.0.0.1:8000/train')
    return Response(r.json())


@api_view(['POST'])
def post_predict(request):
    r = requests.post('http://127.0.0.1:8000/predict', data=request.data)
    return Response(r.json())