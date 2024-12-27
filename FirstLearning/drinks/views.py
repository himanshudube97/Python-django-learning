from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view

@api_view(["GET", 'POST']) #decorator
def drink_list(request):

    if(request.method == "GET"):
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({"drinks":serializer.data}, safe=False)    
    

    if(request.method == "POST"):
        serializer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(["GET","PUT", "DELETE"])
def drink_detail(request, id):  #id is the param in the url
    try:
    
        drink= Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(request.method == "GET"):
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
