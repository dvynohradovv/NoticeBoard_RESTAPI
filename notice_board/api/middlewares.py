from django.utils import timezone
from .models import User, UserDetail
from .signals import userdetails_create


class UpdateLastActivity:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        if not hasattr(request, 'user'):
            return response

        if request.user.is_authenticated:
            try:
                user = UserDetail.objects.get(user=request.user)
            except UserDetail.DoesNotExist:
                userdetails_create(User, request.user, True)
                user = UserDetail.objects.get(user=request.user)
            user.last_request = timezone.now()
            user.save()

        return response
