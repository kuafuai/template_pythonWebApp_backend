from flask import Flask, request, jsonify, make_response
import csv

app = Flask(__name__)

# define route to save form data
@app.route('/save_form_data', methods=['POST'])
def save_form_data():
    # get form data from request
    form_data = request.get_json()

    # save form data to database or perform any other operations

    return jsonify({'message': 'Form data saved successfully'})

# define route to get form data
@app.route('/get_form_data', methods=['GET'])
def get_form_data():
    # get form data from database or any other source
    form_data = {'name': 'John Doe', 'email': 'johndoe@example.com'}

    return jsonify(form_data)

# define route to export form data to CSV
@app.route('/export_form_data', methods=['GET'])
def export_form_data():
    # get form data from database or any other source
    form_data = {'name': 'John Doe', 'email': 'johndoe@example.com'}

    # create CSV file
    csv_file = 'form_data.csv'
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Email'])
        writer.writerow([form_data['name'], form_data['email']])

    # return CSV file as response
    response = make_response(csv_file)
    response.headers['Content-Disposition'] = 'attachment; filename=form_data.csv'
    response.headers['Content-Type'] = 'text/csv'

    return response
