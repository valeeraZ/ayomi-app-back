"""Custom HTTPException classes that extend werkzeug.exceptions."""
from werkzeug.exceptions import Unauthorized

_REALM_REGULAR_USERS = "registered_users@mydomain.com"


class ApiUnauthorized(Unauthorized):
    """Raise status code 401 with customizable WWW-Authenticate header."""

    def __init__(
        self,
        description="Unauthorized",
        error=None,
        error_description=None,
    ):
        self.description = description
        self.www_auth_value = self.__get_www_auth_value(error, error_description)
        Unauthorized.__init__(
            self, description=description, response=None, www_authenticate=None
        )

    def get_headers(self, environ):
        return [("Content-Type", "text/html"), ("WWW-Authenticate", self.www_auth_value)]

    def __get_www_auth_value(self, error, error_description):
        realm = _REALM_REGULAR_USERS
        www_auth_value = f'Bearer realm="{realm}"'
        if error:
            www_auth_value += f', error="{error}"'
        if error_description:
            www_auth_value += f', error_description="{error_description}"'
        return www_auth_value
