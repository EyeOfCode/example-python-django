from functools import wraps
from django.http import JsonResponse
from members_app.models import Member

def member_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if hasattr(request, 'user') and isinstance(request.user, Member):
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({'error': 'Member authentication required'}, status=401)
    return _wrapped_view

def member_role_required(required_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if (
                hasattr(request, 'user')
                and isinstance(request.user, Member)
                and request.user.role in required_roles
            ):
                return view_func(request, *args, **kwargs)
            else:
                return JsonResponse({'error': 'Unauthorized'}, status=403)
        return _wrapped_view
    return decorator
