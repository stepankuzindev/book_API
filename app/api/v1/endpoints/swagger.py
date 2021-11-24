from flask import Flask, jsonify

from app.main import app, spec


@app.route("/api/swagger.json")
def create_swagger_spec() -> Flask.response_class:
    return jsonify(spec.to_dict())
