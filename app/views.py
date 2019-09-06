from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView, ObtainJSONWebToken

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
        _status = 200
    else:
        result = {"detail": "Invalid Token"}
        _status = 401

    return JsonResponse(result, status=_status)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def test(request):
    o = ObtainJSONWebToken(JSONWebTokenAPIView)

    print(request.body)
