from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView

from app.models import BlackList

import jwt


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication, ))
# Create your views here.
def index(request):
    authorization = request.META.get("HTTP_AUTHORIZATION", None)
    token = authorization.split()[1]
    payload = jwt.decode(token, None, None)

    if not BlackList.objects.filter(user__username=payload['username']):
        result = {"token": token}
        status = 200
    else:
        result = {"detail": "Invalid Token"}
        status = 401

    return JsonResponse(result, status=status)


class ObtainJsonWebToken(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer

    print(dir(serializer_class))
