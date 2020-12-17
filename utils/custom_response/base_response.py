from rest_framework.response import Response
from .base_constant import CODE_SUCCESS, MSG_SUCCESS
from rest_framework.status import HTTP_200_OK


class BaseResponse(Response):
    def __init__(self, code=CODE_SUCCESS, message=MSG_SUCCESS, data=None, status=HTTP_200_OK,
                 template_name=None, headers=None, exception=False, content_type=None):
        super(Response, self).__init__(None, status=status)
        if data is None:
            data = {}
        self._code = code
        self._message = message
        self._data = data

        self.data = {"code": code, "msg": message, "data": data}
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in headers.items():
                self[name] = value
