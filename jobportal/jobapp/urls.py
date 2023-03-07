"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from .views import *
urlpatterns = [
    path('index/',index),
    path('send_mail_regis/', send_mail_regis),
    path('success/', success),
    path('registration/', regis),
    path('verify/<auth_token>', verify),
    path('error/', error),
    path('login/', login),
    path('profile/', profile),
    path('post/', postjob),
    path('jobpost/', profile1post),
    path('table/',table),
    path('mailsend/<int:id>',mailsend),
    path('user_reg/',user_register),
    path('user_log/',user_login),
    # path('user_pro/',user_profile),
    # path('edituser/',edituser),
    path('edit<int:id>',edit),
    path('viewjob/<int:id>',viewjob),
    path('viewmore/<int:id>/<int:pk>',view_more),
    path('applyjob/<int:id>/<int:pk>',applyjob)
 ]
