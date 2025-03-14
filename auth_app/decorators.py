from functools import wraps
from django.http import JsonResponse
from members_app.models import Member

def member_login_required(required_roles = []):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request, 'user') and isinstance(request.user, Members):
                if len(required_roles) == 0:
                    return view_func(request, *args, **kwargs)
                if request.user.role in required_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return JsonResponse({'message': 'Permission denied'}, status=403)
            else:
                return JsonResponse({'message': 'Unauthorized'}, status=401)
        return _wrapped_view
    return decorator