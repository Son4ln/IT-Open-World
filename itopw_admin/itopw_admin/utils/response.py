from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_403_FORBIDDEN,
                                   HTTP_404_NOT_FOUND,
                                   HTTP_500_INTERNAL_SERVER_ERROR,
                                   HTTP_503_SERVICE_UNAVAILABLE,
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
        {'message': 'Không có quyền hạn'},
        status=HTTP_403_FORBIDDEN
    )

def response_404():
    return Response(
        {'message': 'Dữ liệu không tồn tại'},
        status=HTTP_404_NOT_FOUND
    )

def response_400(data):
    return Response(
        data,
        status=HTTP_400_BAD_REQUEST
    )

def response_500():
    return Response(
        {"message": "Đã có lỗi xảy ra, vui lòng thử lại"},
        status=HTTP_500_INTERNAL_SERVER_ERROR
    )