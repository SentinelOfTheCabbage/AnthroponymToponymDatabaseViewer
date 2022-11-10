from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for
from flask_security import current_user


class SecuredModelView(ModelView):
    def is_accessible(self):
        return (current_user.is_active and current_user.is_authenticated)

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('security.login'))
