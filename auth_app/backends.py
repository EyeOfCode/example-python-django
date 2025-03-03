from django.contrib.auth.backends import BaseBackend
from members_app.models import Member

class MemberBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None

        if member.check_password(password):
            return member
        return None

    def get_user(self, member_id):
        try:
            return Member.objects.get(pk=member_id)
        except Member.DoesNotExist:
            return None