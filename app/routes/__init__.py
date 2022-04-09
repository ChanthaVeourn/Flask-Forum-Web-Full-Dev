from .view import views
from .auth_view import auth
from .forum_view import forum_blueprint
from .tag_view import tag_blueprint
from .reply_view import reply_blueprint
__all__ = ["views", "auth", "forum_blueprint", "tag_blueprint", "reply_blueprint"]