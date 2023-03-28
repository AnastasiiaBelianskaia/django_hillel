from .models import Logs


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, *args, **kwargs):
        print(request.user.id)
        if not request.path.startswith('/admin'):
            Logs.objects.create(path=request.path_info,
                                method=request.method,
                                user_id=request.user.id,
                                data={'get': request.GET, 'post': request.POST})
