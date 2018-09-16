# importing libraries
from flask import Flask,jsonify
from flask_cors import CORS
from barcode import *

# getting app name
app = Flask(__name__)
CORS(app)



#creating app route and method 'GET'
@app.route('/',methods=['GET'])
def show():
    '''creating a dictionary datatype to return data in JSON format''' 
    response ={
        'info' : file('Screenshot from 2018-09-15 14-57-11.png'),
        'message': 'information extracted'
        }
    
    return jsonify(response),200        #returning response in JSON fromat and Error Code 200



# checking app name is main or not
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
