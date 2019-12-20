"""UserMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', login_views.index),
    path('login/', login_views.login),
    path('register/', login_views.register),
    path('logout/', login_views.logout),

    path('captcha/', include('captcha.urls')),      # 生成验证码图片
]
