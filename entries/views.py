from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from entries import serializers

from entries.models import EntryModel
from entries.serializers import EntrySerializer
from django.shortcuts import get_object_or_404
from entries.models import EntryModel
from rest_framework import status


class EntryListAPI(APIView):
    def get(self,request):
        entries = EntryModel.objects.all()
        
        serializer = EntrySerializer(entries, many=True)
        
        return Response(serializer.data)
    
    
    def post(self, request):
        entry = EntryModel(datetime=request.data.get("datetime"),
                      amount=request.data.get("amount"),
                      concept=request.data.get("concept"))
        
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
            
        return Response(serializer.errors, status=400)


class EntryDetailAPI(APIView):

    def get_entry(self, request, pk):
        user = get_object_or_404(EntryModel, pk=pk)
        return user

    def get(self, request, pk):

        user = self.get_entry(request, pk)

        serializer = EntrySerializer(instance=user)
        return Response(serializer.data)


    def put(self, request, pk):

        #user = User.object.get(pk=pk)
        user = get_object_or_404(EntryModel, pk=pk)

        serializer = EntrySerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk):

        user = get_object_or_404(EntryModel, pk=pk)

        self.check_object_permissions(request, user)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
    
    

