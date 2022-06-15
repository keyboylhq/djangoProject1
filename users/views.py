from django.shortcuts import render
from rest_framework.views import APIView  # API
from .sms_code import send_message
from .models import User  # 导包自带用户
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateUserSerializer, UserDetailSerializer
from rest_framework import mixins,viewsets
from django.contrib.auth import get_user_model
from .rediscli import get_redis_cli
User1 = get_user_model()
#
# class UserView(CreateAPIView):
#     """用户注册"""
#     # 指定序列化器
#     serializer_class = CreateUserSerializer



# 手机认证码
class SMSCodeAPIView(APIView):

    def post(self, request):
        # 1. 接收手机号
        mobile = request.data.get('mobile')
        # mobile = request.POST.get('mobile')

        # 2. 判断手机号是否为空
        if not mobile:
            return Response({'msg': '手机号为空'}, status=400)

        # 3. 判断手机号对应的用户是否存在
        try:
            user = User.objects.get(mobile=mobile)
        except User.DoesNotExist:
            return Response({'msg': '该手机号未注册'}, status=400)

        # 4. 获取redis客户端
        redis_cli = get_redis_cli()

        # 4.1 获取短信验证码标志
        flag = redis_cli.get('flag_%s' % mobile)

        # 4.2 验证短信发送标志是否存在
        if flag:
            return Response({'msg': "短信发送过于频繁"}, status=400)

        # 5. 生成短信验证码
        code = '%06d' % random.randint(0, 999999)

        # 5.1 验证码存入redis，设置过期时间为10min
        redis_cli.set('code_%s' % mobile, code, ex=600)

        # 5.2 发送标志存入redis， 设置过期时间为1min
        redis_cli.set('flag_%s' % mobile, 1, ex=60)

        # 6. 发送短信验证码
        send_message(mobile, code)

        # 7.返回响应
        return Response({'msg': '发送成功'}, status=200)

def img_code(request):

    redis_cli_img = get_redis_cli()
    imgcode  = "12323"
    flag = redis_cli_img.get('flag_%s' % imgcode)
    # redis_cli_img.set('code_%s' % imgcode, code, ex=600)


class UserView(mixins.CreateModelMixin,viewsets.GenericViewSet):
    """用户注册"""
    # 指定序列化器
    serializer_class = CreateUserSerializer
    queryset = User1.objects.all()