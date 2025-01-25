from flask import request, jsonify
from app import app, db
from app.models.requests_test import Requests


@app.route('/test', methods=['POST'])
def create_request():
    data = request.get_json()
    

# if __name__ == '__main__':
#     app.run(debug=True)