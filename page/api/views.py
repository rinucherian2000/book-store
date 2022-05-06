from django.shortcuts import render
from owner.models import Books
from rest_framework.views import APIView
from api.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BookView(APIView):
    def get(self,request,*args,**kwargs):
        book=Books.objects.all()
        serializer=BookSerializer(book,many=True)
        return Response(serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class BookList(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(book)
        return Response(serializer.data)

    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerializer(instance=book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        book.delete()
        return Response({"message:delete"})















