from flask import current_app as app
import requests
from flask import request
from flask_restful import Resource, Api
from database import getPlantComments, addComment, createPlant
from flask import jsonify

api = Api(app)
ERROR = jsonify({"status": "error", "message": "please check the code"})
class CommentList(Resource):
    def get(self, pid):
        try:
            comments = getPlantComments(pid)
            result = {"comments": comments, "status": "success"}
            return jsonify(result)
        except:
            return ERROR
    
    def post(self, pid):
        print(request.json)
        try:
            uid = request.json["uid"]
            comment = request.json["comment"]
            addComment(pid, uid, comment)
            return {"status": "success"}
        except:
            return ERROR

    def put(self, pid):
        try:
            createPlant(pid)
            return {"status": "success"}
        except:
            return ERROR
    

    
        


class User(Resource):
    def post(self, user):
        pass

    def get(self, user):
        pass



api.add_resource(CommentList, "/comments/<pid>")
api.add_resource(User, "/addUser/<user>")