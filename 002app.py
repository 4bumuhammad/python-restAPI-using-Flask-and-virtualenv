from crypt import methods
from urllib import response
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app=Flask(__name__)

api=Api(app)

CORS(app)

identitas={} 

class ContohResource(Resource):

    def post(self):
        nama=request.form["nama"] 
        umur=request.form["umur"]
        identitas["nama"]=nama
        identitas["umur"]=umur
        response={"msg":"Data berhasil dimasukkan"} 
        return response 

    def get(self):
        return identitas
 
api.add_resource(ContohResource, "/api", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
