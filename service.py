from flask import Flask, request, jsonify
from flask_cors import CORS

import json
import csvManipulate as csv
app = Flask(__name__)
CORS(app)
@app.route('/Energia', methods=['GET', 'POST'])
def energia():
    """Handles GET E POST /Energia endpoint."""

    if request.method == 'GET':
        user_id = request.args.get('id')
        if user_id is None:
            return jsonify({'error': 'Missing user id parameter.'}), 400

        try:
            response_data = csv.getAll(user_id)
            return jsonify(response_data), 200
        except ValueError:
            return jsonify({'error': 'Algum erro'}), 400

    elif request.method == 'POST': 
        try:
            content_type = request.headers.get('Content-Type')
            if content_type != 'application/json':
                return jsonify({'error': 'Invalid request content type. Please send JSON data.'}), 400

            request_data = request.get_data()
            if not request_data:
                return jsonify({'error': 'Empty request data. Please provide data in JSON format.'}), 400
            try:
                dadosRecebidos = json.loads(request_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {e}")
                return jsonify({'error': 'Invalid JSON data format.'}), 400

            print('Dados recebidos:', dadosRecebidos)
            csv.updateDataframe(dadosRecebidos)
            return jsonify({'message': 'Dados recebidos e registrados com sucesso!'}), 200
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify({'error': 'An internal server error occurred.'}), 500
    else:
        return jsonify({'error': 'Unsupported HTTP method'}), 405

@app.route('/Login', methods=['POST'])
def login():
    """Handles POST /Login endpoint."""
    if request.method == 'POST':
        try:
            content_type = request.headers.get('Content-Type')
            if content_type != 'application/json':
                return jsonify({'error': 'Invalid request content type. Please send JSON data.'}), 400

            request_data = request.get_data()
            if not request_data:
                return jsonify({'error': 'Empty request data. Please provide data in JSON format.'}), 400
            try:
                dadosRecebidos = json.loads(request_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {e}")
                return jsonify({'error': 'Invalid JSON data format.'}), 400

            print('Dados recebidos:', dadosRecebidos)
            result = csv.login(dadosRecebidos)
            return jsonify({'result': str(result) }), 200
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify({'error': 'An internal server error occurred.'}), 500
    else:
        return jsonify({'error': 'Unsupported HTTP method'}), 405

@app.route('/Meta', methods=['POST'])
def create_meta():
    """Handles POST /Meta"""
    try:
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return jsonify({'error': 'Invalid request content type. Please send JSON data.'}), 400

        request_data = request.get_data()
        if not request_data:
            return jsonify({'error': 'Empty request data. Please provide data in JSON format.'}), 400
        
        try:
            dados_recebidos = json.loads(request_data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON data: {e}")
            return jsonify({'error': 'Invalid JSON data format.'}), 400

        if not all(key in dados_recebidos for key in ['IdUser', 'Month', 'Meta']):
            return jsonify({'error': 'Missing required fields: IdUser, Month, Meta.'}), 400

        message = csv.createMeta(dados_recebidos)
        
        return jsonify({'message': message}), 200

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)