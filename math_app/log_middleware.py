from .models import Logs


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, *args, **kwargs):
        if request.path.startswith('/admin'):
            pass
        else:
            data = Logs(path=request.path_info,
                        method=request.method,
                        user=request.user,
                        data={'get': request.GET, 'post': request.POST})
            data.save()
