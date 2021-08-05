from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
app = Flask(__name__)
api = Api(app)

class Bloomberg(Resource):
    def get(self):
        data = pd.read_csv('BDO-Securities-BB.csv')  # read CSV
        
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('ISIN', required=True)  # add args
        parser.add_argument('Date', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        
        vSecID = args['ISIN']
        vDate = args['Date']
        
        data = data.query('SecurityID== @vSecID and Date == @vDate').head()
        
        #data = data.to_dict()  # convert dataframe to dictionary
        
        data = data.to_csv(index=False , header=False)  # convert dataframe to dictionary

        return {'data': data}, 200  # return data and 200 OK code

    pass
    
    
api.add_resource(Bloomberg, '/BB')  # '/users' is our entry point


class Reuters(Resource):
    def get(self):
        data = pd.read_csv('BDO-Securities-REUTERS.csv')  # read CSV
        
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('ISIN', required=True)  # add args
        parser.add_argument('Date', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        
        vSecID = args['ISIN']
        vDate = args['Date']
        
        data = data.query('SecurityID== @vSecID and Date == @vDate').head()
        
        #data = data.to_dict()  # convert dataframe to dictionary
        
        data = data.to_csv(index=False , header=False)  # convert dataframe to dictionary

        return {'data': data}, 200  # return data and 200 OK code

    pass
    
    
api.add_resource(Reuters, '/REUTERS')  # '/users' is our entry point



class IDC(Resource):
    def get(self):
        data = pd.read_csv('BDO-Securities-IDC.csv')  # read CSV
        
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('ISIN', required=True)  # add args
        parser.add_argument('Date', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        
        vSecID = args['ISIN']
        vDate = args['Date']
        
        data = data.query('SecurityID== @vSecID and Date == @vDate').head()
        
        #data = data.to_dict()  # convert dataframe to dictionary
        
        data = data.to_csv(index=False , header=False)  # convert dataframe to dictionary

        return {'data': data}, 200  # return data and 200 OK code

    pass
    
    
api.add_resource(IDC, '/IDC')  # '/users' is our entry point



class Markit(Resource):
    def get(self):
        data = pd.read_csv('BDO-Securities-MARKIT.csv')  # read CSV
        
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('ISIN', required=True)  # add args
        parser.add_argument('Date', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        
        vSecID = args['ISIN']
        vDate = args['Date']
        
        data = data.query('SecurityID== @vSecID and Date == @vDate').head()
        
        #data = data.to_dict()  # convert dataframe to dictionary
        
        data = data.to_csv(index=False , header=False)  # convert dataframe to dictionary

        return {'data': data}, 200  # return data and 200 OK code

    pass
    
    
api.add_resource(Markit, '/MARKIT')  # '/users' is our entry point


if __name__ == '__main__':
    app.run()  # run our Flask app