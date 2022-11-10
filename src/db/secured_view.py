from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_security import current_user


class SecuredMixin():
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated)

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('security.login'))


class SecuredModelView(SecuredMixin, ModelView):
    pass


class AdminMixin():
    def is_accessible(self):
        return current_user.is_active and\
            current_user.is_authenticated and\
            'admin' in [role.name for role in current_user.roles]

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('admin'))


class AdminModelView(AdminMixin, ModelView):
    pass
