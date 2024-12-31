from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from blogProject.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny

class Auth(ViewSet):
    # permission_classes = [AllowAny] 
    # """
    # A ViewSet that handles multiple actions like creating users and posts.
    # """


    # ## Writing the functions here. permission_classes = [AllowAny]
    @api_view(['POST'])
    def createUser(self, request):
        print(request, "request")
        return Response({"data":{},    'message': 'User created successfully'}, status=status.HTTP_200_OK)
            ## sending to serielizer
        serializer = UserSerializer(data=request.data)
    #     if(serializer.is_valid()):
    #         ## extracting valid data
    #         email = serializer.validated_data.get('email')
    #         password = serializer.validated_data.get('password')
    #         confirm_password = serializer.validated_data.get('confirm_password')

    #         ## checking if password and confirm password are same
    #         if(password != confirm_password):
    #             return Response({"data":{},    'message': 'Password and Confirm Password do not match'}, status=status.HTTP_400_BAD_REQUEST)
            
    #         ##checking if user already exists
    #         user = User.objects.filter(email=email).first()

    #         if(user):
    #             return Response({"data":{},    'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
    #         ## creating user
    #         user = User.objects.create_user(email=email, password=password)
    #         user.save()
    #         return Response({"data":user,    'message': 'User created successfully'}, status=status.HTTP_200_OK)

    # ## when serielzier is not valid
    #     return Response({"data":{},    'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)

        

