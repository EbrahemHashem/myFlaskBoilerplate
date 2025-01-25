from flask_restx import Api
from flask import Blueprint

from .user.controller import api as user_ns
from .test.controller import api as request_ns


# Import controller APIs as namespaces.
api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="API", description="Main routes.")

# API namespaces
api.add_namespace(user_ns,"/user")
api.add_namespace(request_ns,"/request")