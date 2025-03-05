from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .models import CustomUser
# Create your views here.

@api_view(['POST'])
def signup(request):
    """Registering New Users."""
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    "User Login With Authentication Tokens"
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass
        if not user:
            user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)      

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    "Log's Out the User"
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Succcessfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'erroe': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        