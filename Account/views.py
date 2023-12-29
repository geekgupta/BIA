# views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import  UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate




class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]
    

    def post(self, request, *args, **kwargs):
        data = request.data
        user = authenticate(username =data['username'], password=data['password'])
        
        """  JWT Implementation is commented because of simplicity   
        
        print("**************" , request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data


        refresh = RefreshToken.for_user(user)        
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)
        return Response({
            'access_token': access_token,
            'refresh_token': refresh_token,
        })   """
        
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

