from rest_framework.response import Response
from django.utils.translation import ugettext_lazy as _
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR)


def response_200(data):
    return Response(
        data,
        status=HTTP_200_OK
    )


def response_201(data):
    return Response(
        data,
        status=HTTP_201_CREATED
    )


def response_403():
    return Response(
        {'message': _("Permission Deny")},
        status=HTTP_403_FORBIDDEN
    )


def response_404():
    return Response(
        {'message': _("Not Found")},
        status=HTTP_404_NOT_FOUND
    )


def response_400(data):
    return Response(
        data,
        status=HTTP_400_BAD_REQUEST
    )


def response_500():
    return Response(
        {"message": _("Server Error")},
        status=HTTP_500_INTERNAL_SERVER_ERROR
    )
