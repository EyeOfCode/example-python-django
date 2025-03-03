from django.utils.deprecation import MiddlewareMixin
from .utils import verify_jwt_token
from members_app.models import Member

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            member_id = verify_jwt_token(token)
            if member_id:
                try:
                    member = Member.objects.get(id=member_id)
                    request.user = member
                except Member.DoesNotExist:
                    pass
        return None