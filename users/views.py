from django.shortcuts import render
from django.contrib.auth import login

# from django.views.generic import FormView

# from .forms import LoginForm
from rest_framework import viewsets
from rest_framework.decorators import action
from django.views.generic import CreateView
from django.shortcuts import render

# Create your views here.
from djoser.views import UserViewSet
from .models import User
from .serializers import CustomUserSerializer, GroupSerializer
from django.urls import reverse_lazy
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy("services:index")
    template_name = "users/signup.html"


class CustomUserViewSet(UserViewSet):
    pass


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer

    def get_queryset(self):
        # Получаем id тренера/админа из эндпоинта
        user_id = self.kwargs.get("user_id")
        # И отбираем группу, где он админ
        new_queryset = Group.objects.filter(admin=user_id)
        return new_queryset

        sportsmen = User.objects.filter(role=ROLE_CHOICES.SPORTSMEN.value)

    @action(detail=False)
    def filling_group(self):
        admin = request.user
        sportsmen = User.objects.filter(role=ROLE_CHOICES.SPORTSMEN.value)

        serializer = GroupSerializer(sportsmen, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

        Group.objects.create(admin=admin, sportsmen=sportsmen)
        return Response(serializer.data, status=HTTP_201_CREATED)


# class UserLogin(FormView):
#     queryset = User.objects.all()
#     form_class = LoginForm
#     template_name = "users/signup.html"

#     def form_valid(self, form):
#         user = User.objects.filter(username=form.cleaned_data["username"])
#         if user is None:
#             return HttpResponseRedirect("/login")
#         if not user.check_password(form.cleaned_data["password"]):
#             return HttpResponseRedirect("/login")
#         login(self.request, user)
#         return HttpResponseRedirect("/")
