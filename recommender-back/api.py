from flask import Flask, jsonify

api = Flask(__name__)

@api.route('/', methods=['GET'])
def index():
    data = {
        'message': 'Hello from the backend!',
        'status': 200
        }
    
    return jsonify(data)

if __name__ == '__main__':
    api.run(debug=True)