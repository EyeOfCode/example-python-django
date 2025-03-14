from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from auth_app.backends import MemberBackend
from members_app.models import Member
from members_app.serializers import MemberSerializer
from .utils import generate_jwt_token
from .decorators import member_login_required

# Create your views here.
@api_view(['POST'])
def Login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    member_backend = MemberBackend()
    member = member_backend.authenticate(request, username, password)
    if member is not None:
        token = generate_jwt_token(member.id)
        return Response({'token': token}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def Register(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@member_login_required()
def GetMembers(request):
    member = request.user
    serializer = MemberSerializer(member)
    return Response(serializer.data, status=status.HTTP_200_OK)
