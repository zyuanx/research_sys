from django.http import Http404
from rest_framework.exceptions import ValidationError, NotAuthenticated
from rest_framework.views import exception_handler
from rest_framework_simplejwt.exceptions import InvalidToken


def get_key_and_value(detail):
    msg = []
    for key, value in detail.items():
        msg.append(str(key) + str(value[0]))
    return '\n'.join(msg)


def custom_exception_handler(exc, context):
    ret = {'code': 200, 'msg': '', 'data': {}}
    response = exception_handler(exc, context)
    if isinstance(exc, ValidationError):
        ret['code'] = exc.status_code
        ret['msg'] = get_key_and_value(exc.detail)
        response.data = ret
    elif isinstance(exc, NotAuthenticated):
        ret['code'] = exc.status_code
        ret['msg'] = exc.detail
        response.data = ret
    elif isinstance(exc, InvalidToken):
        if exc.detail.get('code') == 'token_not_valid':
            ret['code'] = exc.status_code
            ret['msg'] = '认证信息不合法或者已失效。'
            response.data = ret
        else:
            ret['code'] = exc.status_code
            ret['msg'] = '未知错误。'
    elif isinstance(exc, Http404):
        ret['code'] = 200
        ret['msg'] = '未找到'
        response.data = ret
    return response

# | *状态码* | *含义*                | *说明*                                              |
# | -------- | --------------------- | --------------------------------------------------- |
# | 200      | OK                    | 请求成功                                            |
# | 201      | CREATED               | 创建成功                                            |
# | 204      | DELETED               | 删除成功                                            |
# | 400      | BAD REQUEST           | 请求的地址不存在或者包含不支持的参数                |
# | 401      | UNAUTHORIZED          | 未授权                                              |
# | 403      | FORBIDDEN             | 被禁止访问                                          |
# | 404      | NOT FOUND             | 请求的资源不存在                                    |
# | 422      | Unprocesable entity   | [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误 |
# | 500      | INTERNAL SERVER ERROR | 内部错误                                            |
