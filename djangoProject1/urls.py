
from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url,include
from rest_framework import routers
from users.views import UserView
router = routers.DefaultRouter()
router.register(r'user',UserView,basename="user")
# router.register(r'email',EmailRegviewsSet,basename="email")
from users import views


urlpatterns = [
    # 管理
    path('admin/', admin.site.urls),
    # url集合
    url('', include(router.urls)),
    # 短信认证码
    url(r'^sms/$', views.SMSCodeAPIView.as_view()),
    # # 短信登录
    # url(r'^smslonin/$', views.SMSCodeLoginAPIView.as_view()),
    # # 三端登录
    path('login/', obtain_jwt_token),
    path('imgcode/', views.img_code),
]
