from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from auth_app.decorators import member_login_required
from .models import Member
from .serializers import MemberSerializer

# Create your views here.
@api_view(['POST'])
def MemberCreate(request):
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def MemberUpdate(request, id):
    try:
        data = Member.objects.get(id=id)
    except Member.DoesNotExist:
        return Response({'error': 'Member not found'},status=status.HTTP_404_NOT_FOUND)
    serializer = MemberSerializer(data, data=request.data, partial=True, context={'exclude': ['username', 'email']})
    if serializer.is_valid():
        if request.data.get('password'):
            serializer.validated_data['password'] = make_password(request.data.get('password'))
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def MemberDelete(request, id):
    try:
        data = Member.objects.get(id=id)
    except Member.DoesNotExist:
        return Response({'error': 'Member not found'},status=status.HTTP_404_NOT_FOUND)
    data.delete()
    return Response({'message': 'Member deleted'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@member_login_required(required_roles=['admin'])
def MemberList(request):
    data = Member.objects.all()
    serializer = MemberSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@member_login_required()
def MemberDetail(request, id):
    try:
        data = Member.objects.get(id=id)
    except Member.DoesNotExist:
        return Response({'error': 'Member not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MemberSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)