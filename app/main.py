from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)


spec = APISpec(
    title="flask-api-swagger-doc",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

from app.api.v1.endpoints.author import add_author, get_authors  # noqa
from app.api.v1.endpoints.book import add_book, get_books  # noqa
from app.api.v1.endpoints.swagger import create_swagger_spec  # noqa
from app.api.v1.endpoints.todo import todo  # noqa

with app.test_request_context():
    spec.path(view=todo)  # noqa

    spec.path(view=get_authors)  # noqa
    spec.path(view=add_author)  # noqa

    spec.path(view=get_books)  # noqa
    spec.path(view=add_book)  # noqa


SWAGGER_URL = "/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = "http://0.0.0.0:8000/api/swagger.json"  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Book API"},  # Swagger UI config overrides
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)
