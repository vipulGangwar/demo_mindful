from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test_form
from .serializers import Test_formSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def test_form_collection(request):
    if request.method == 'GET':
        Test_form_data = Test_form.objects.all()
        serializer = Test_formSerializer(Test_form_data, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        #form_data = Test_formSerializer(data=request.data)
        serializer = Test_formSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
