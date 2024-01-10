from flask import request, jsonify
from app import app
from app.models import FormData, export_to_csv

@app.route('/api/form', methods=['POST'])
def save_form_data():
    data = request.get_json()
    if 'name' not in data or 'email' not in data or 'message' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    form_data = FormData(data['name'], data['email'], data['message'])
    form_data.save()
    return jsonify(form_data.serialize()), 201

@app.route('/api/form', methods=['GET'])
def get_form_data():
    form_data = FormData.get_all()
    if not form_data:
        return jsonify({'message': 'No form data available'}), 404
    return jsonify(form_data), 200

@app.route('/api/form/export', methods=['GET'])
def export_form_data():
    form_data = FormData.get_all()
    if not form_data:
        return jsonify({'message': 'No form data available for export'}), 404
    csv_file = export_to_csv(form_data)
    return csv_file, 200
