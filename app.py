# import library
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

    def get(self):
        #response={"msg":"Hallo dunia, ini app restful pertamaku"}

        return identitas
 
    def post(self):
        nama=request.form["nama"] 
        umur=request.form["umur"]
        identitas["nama"]=nama
        identitas["umur"]=umur
        response={"msg":"Data berhasil dimasukkan"} 
        return response 

# setup resourcenya
api.add_resource(ContohResource, "/api", methods=["GET","POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
