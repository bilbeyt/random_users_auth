from accounts.models import CustomUser
from rest_framework.exceptions import NotFound


class APIRequestCheck:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        key = request.META.get("HTTP_API_KEY", "")
        if CustomUser.objects.filter(api_key=key).exists():
            return self.get_response(request)
        else:
            return NotFound