"""Parsers and serializers for /auth API endpoints."""
from flask_restx import Model
from flask_restx.fields import String
from flask_restx.inputs import email
from flask_restx.reqparse import RequestParser


auth_reqparser = RequestParser(bundle_errors=True)
auth_reqparser.add_argument(
    name="email", type=email(), location="form", required=True, nullable=False
)
auth_reqparser.add_argument(
    name="password", type=str, location="form", required=True, nullable=False
)

modify_reqparser = RequestParser(bundle_errors=True)
modify_reqparser.add_argument(
    name="new_email", type=email(), location="form", required=True, nullable=False
)

user_model = Model(
    "User",
    {
        "email": String,
        "token_expires_in": String,
    },
)
