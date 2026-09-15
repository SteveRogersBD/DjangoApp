from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET","POST"])
def user_list(request):
    if request.method == "GET":
        return Response({"message": "Hello World"})
    
    elif request.method == "POST":
        return Response({"message": "Hello World POST"})

@api_view(["GET","PUT","DELETE"])
def user_detail(request,pk):
    if request.method == "GET":
        return Response({"message": "Hello World"})
    elif request.method == "PUT":
        return Response({"message": "Hello World PUT"})
    elif request.method == "DELETE":
        return Response({"message": "Hello World DELETE"})
