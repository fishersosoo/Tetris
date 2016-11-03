#encoding=utf-8
import flask_restful as restful
from flask import Flask, jsonify
from flask import make_response
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
    from resources.rank import RankList, Rank
    from resources import HelloWorld
    api.add_resource(Rank, '/rank/')
    api.add_resource(RankList, '/ranklist/')
    api.add_resource(HelloWorld, '/')
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'message':'Not found'}),404)
    @app.errorhandler(500)
    def not_found(error):
        return make_response(jsonify({'message': 'Error'}), 500)