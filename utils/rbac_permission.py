from rest_framework.permissions import BasePermission


class RbacPermission(BasePermission):
    """
    基于角色的认证系统的权限校验类
    """

    @classmethod
    def get_permission_from_role(cls, request):
        try:
            perms = request.user.roles.values('permissions__method').distinct()
            return [p['permissions__method'] for p in perms]
        except AttributeError:
            return None

    def has_permission(self, request, view):
        """
        权限校验逻辑
        :param request:
        :param view:
        :return:
        """
        if not hasattr(view, 'permission_prefix'):
            return True

        perms = self.get_permission_from_role(request)
        if not perms:
            return False

        perms_prefix = view.permission_prefix
        _method = view.action
        if perms_prefix + '_' + _method in perms:
            return True
        else:
            return False
