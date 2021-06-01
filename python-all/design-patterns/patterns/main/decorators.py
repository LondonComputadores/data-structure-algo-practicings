from .utils import is_logged_in


def login_required(func):

    def wrapped_func(request, *args, **kwargs):
        request = is_logged_in(request)

        resp = func(request, *args, **kwargs)

        return resp

    return wrapped_func