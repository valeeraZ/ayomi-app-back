"""Decorators that decode and verify authorization tokens."""
from functools import wraps

from flask import request

from ..exceptions import ApiUnauthorized
from ...models.user import User


def token_required(f):
    """Execute function if request contains valid access token."""

    @wraps(f)
    def decorated(*args, **kwargs):
        token_payload = _check_access_token()
        for name, val in token_payload.items():
            setattr(decorated, name, val)
        return f(*args, **kwargs)

    return decorated


def _check_access_token():
    token = request.headers.get("Authorization")
    if not token:
        raise ApiUnauthorized(description="Unauthorized")
    result = User.decode_access_token(token)
    if result.failure:
        raise ApiUnauthorized(
            description=result.error,
            error="invalid_token",
            error_description=result.error,
        )
    return result.value
