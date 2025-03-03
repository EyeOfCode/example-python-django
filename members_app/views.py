from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from auth_app.decorators import member_login_required, member_role_required
from .models import Member
from .serializers import MemberSerializer

# Create your views here.
@api_view(['GET'])
@member_login_required
@member_role_required(required_roles=['admin'])
def MemberList(request):
    data = Member.objects.all()
    serializer = MemberSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@member_login_required
def MemberDetail(request, id):
    try:
        data = Member.objects.get(id=id)
    except Member.DoesNotExist:
        return Response({'error': 'Member not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MemberSerializer(data)
    return Response(serializer.data, status=status.HTTP_200_OK)