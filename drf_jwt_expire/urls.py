from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

from app.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', test),
    path('api/token/verify/', verify_jwt_token),
    path('api/app/', include('app.urls'))
]
