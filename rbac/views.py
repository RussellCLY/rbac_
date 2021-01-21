from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.

def login(request):
    username = request.GET.get('u')
    user_obj = models.User.objects.get(username=username)
    # 方式一
    # m = models.ManyToManyField('Role')
    # role_list = user_obj.m.all() # [Role(),Role]

    # 方式二
    # user2role_list = models.User2Role.objects.filter(u=user_obj)

    # 方式三
    models.Role.objects.filter(a='...')

    return HttpResponse('......')