from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jsonify
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint
from marshmallow import Schema, fields

app = Flask(__name__)
api = Api(app)


spec = APISpec(
    title="flask-api-swagger-doc",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)


@app.route("/api/swagger.json")
def create_swagger_spec() -> Flask.response_class:
    return jsonify(spec.to_dict())


class TodoResponseSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    status = fields.Boolean()


class TodoListResponseSchema(Schema):
    todo_list = fields.List(fields.Nested(TodoResponseSchema))


@app.route("/todo")
def todo() -> Flask.response_class:
    """Get List of Todo
    ---
    get:
        description: Get List of Todos
        responses:
            200:
                description: Return a todo list
                content:
                    application/json:
                        schema: TodoListResponseSchema
    """

    dummy_data = [
        {"id": 1, "title": "Finish this task", "status": False},
        {"id": 2, "title": "Finish that task", "status": True},
    ]

    return TodoListResponseSchema().dump({"todo_list": dummy_data})


with app.test_request_context():
    spec.path(view=todo)


SWAGGER_URL = "/docs"  # URL for exposing Swagger UI (without trailing '/')
API_URL = "http://0.0.0.0:8000/api/swagger.json"  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={"app_name": "Test application"},  # Swagger UI config overrides
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
