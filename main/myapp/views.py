from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View


class ComplexFeatureMixin:
    @login_required
    def perform_complex_action(self, request):
        # Этот метод будет доступен только для зарегистрированных пользователей
        return HttpResponse("Complex action performed successfully.")


class MyMixin(ComplexFeatureMixin, View):
    pass

