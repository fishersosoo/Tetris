#encoding=utf-8
import flask_restful as restful
from flask import jsonify
from flask.ext.restful import reqparse

from restful_app import Session
from restful_app import api
from restful_app.model.player import Player


class RankList(restful.Resource):
    def get(self):
        player = Session.query(Player).all()
        player_list=list()
        for one in player:
            player_list.append({'name':one.PlayerName,'score':one.Score})
        print jsonify(player_list)
        return jsonify({'list':player_list})


class Rank(restful.Resource):
    put_parser = reqparse.RequestParser()
    put_parser.add_argument(
        'name', dest='name',
        type=str, location='values',
        required=True, help='The player\'s username',
    )
    put_parser.add_argument(
        'score', dest='score',
        type=int, location='values',
        required=True, help='The player\'s username',
    )

    get_parser = reqparse.RequestParser()
    get_parser.add_argument(
        'name', dest='name',
        type=str, location='values',
        required=True, help='The player\'s username',
    )

    @api.representation('application/json')
    def get(self):
        try:
            args=Rank.get_parser.parse_args()
        except:
            return jsonify({'message':"args error"})
        name=args.name
        play = Session.query(Player).filter(Player.PlayerName == name).all()
        if len(play) == 0:
            return jsonify({"message": "no player"})
        play=play[0]
        #return jsonify({"message": "no player"})
        return jsonify({'name':play.PlayerName,'score':play.Score})

    @api.representation('application/json')
    def put(self):
        try:
            args = Rank.put_parser.parse_args()
        except Exception:
            return jsonify({'message':"args error"})
        name=args.name
        s=int(args.score)
        play = Session.query(Player).filter(Player.PlayerName==name).one()
        if play == None:
            play = Player(PlayerName=name, Score=s)
            Session.add(play)
            Session.commit()
        else:
            if play.Score < s:
                play.Score = s
                Session.commit()
                return jsonify({"message": 'new record'})
        return jsonify({"message": 'success'})
