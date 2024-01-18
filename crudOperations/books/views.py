from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# READ
@api_view(['GET'])
def Bookslist(request): # function-based-view
    booksobj = BooksModel.objects.all() #querset
    serializer = BookSerializer(booksobj,many=True) #serializer 
    return Response(serializer.data)
#CREATE
@api_view(['POST'])
def Create_book(request):
    booksobj = BooksModel.objects.all()
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#UPDATE
@api_view(['POST'])
def Update_book(request,id):
    booksobj = BooksModel.objects.get(id=id)
    serializer = BookSerializer(instance=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#DELETE
@api_view(['DELETE'])
def Delete_book(request,id):
    booksobj = BooksModel.objects.get(id=id)
    booksobj.delete()
    return Response("id={0} book is deleted".format(id))
    

