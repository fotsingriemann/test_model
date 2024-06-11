from django.contrib import admin
from django.urls import path, re_path
from helloworld import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Hello, world!
    re_path(r'^model_testing/(?P<latitude>\d+\.\d+)/(?P<longitude>\d+\.\d+)/$', views.model_testing, name='model_testing'),
]
