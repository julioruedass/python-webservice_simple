from flask import Flask, jsonify
from model_users import users

app = Flask(__name__)

@app.route('/',methods=['GET'] )
def hello():
    return jsonify({'status': 'active','message': 'index','code':200})

@app.route('/home',methods=['GET'])
def home():
    return jsonify({"status": "active","message": "home","code":200})

@app.route('/users',methods=['GET'])
def r_users():
    return jsonify({"status": "active","message": "usuarios","code":200,"users": users })

@app.route('/error',methods=['GET'])
def error():
    return jsonify({"status": "inactive","message": "error","code":0})
 
if __name__ == '__main__':  
    app.run(host="0.0.0.0",port=4000, debug=True) 