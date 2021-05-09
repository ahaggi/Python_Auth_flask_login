from . import login_manager
from .models import User


@login_manager.user_loader
def load_user(user_id):
    """Flask-login will try to load a user BEFORE every request that target a route decorated by ."""
    if user_id is not None:
        return User.query.filter(User.id == user_id).first()
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Dealing with unauthorized users"""
    return {"errMsg" : "Missing credentials! Please log in." } , 403
