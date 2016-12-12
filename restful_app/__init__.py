#encoding=utf-8
import flask_restful as restful
from flask import Flask, jsonify
from flask import make_response
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///table.db'
db = SQLAlchemy(app)
api = restful.Api(app)
db.create_all()
Session=db.session()
Session.commit()
def init_db(db):
    import model.player
    db.create_all()
    Session = db.session()
    Session.commit()

def register_resource(api):
    from resources.rank import RankList, Rank,LocalRankList
    from resources import HelloWorld
    api.add_resource(Rank, '/rank/')
    api.add_resource(RankList, '/ranklist/')
    api.add_resource(LocalRankList,'/localranklist/')
    api.add_resource(HelloWorld, '/')
    @app.errorhandler(404)
    def not_found(error=None):
        message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 404
        return resp
    @app.errorhandler(500)
    def not_found(error):
        message = {
            'status': 500,
            'message': 'Error in: ' + request.url,
        }
        resp = jsonify(message)
        resp.status_code = 500
        return resp