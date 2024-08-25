from django.contrib import admin
from django.urls import path
from applast.views import index, Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('register/', Register.as_view(), name='register'),
]
