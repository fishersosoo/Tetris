#encoding=utf-8
import flask_restful as restful
from flask import jsonify


class HelloWorld(restful.Resource):
    def get(self):
        return jsonify({'hello': 'world'})

