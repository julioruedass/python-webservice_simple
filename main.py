from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'status': 'active','message': 'index','code':200})

@app.route('/home')
def home():
    return jsonify({'status': 'active','message': "home",'code':200})

@app.route('/error')
def error():
    return jsonify({'status': 'inactive','message': "error",'code':0})
 
if __name__ == '__main__':
    app.run() 