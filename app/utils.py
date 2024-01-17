from flask import Flask, request, jsonify, make_response
import csv

app = Flask(__name__)

# route to save form data
@app.route('/save', methods=['POST'])
def save_form_data():
    # get form data from request
    form_data = request.get_json()

    # save form data to database or any other storage

    return jsonify({'message': 'Form data saved successfully'})

# route to get form data
@app.route('/get', methods=['GET'])
def get_form_data():
    # get form data from database or any other storage

    # return form data as JSON response
    return jsonify(form_data)

# route to export form data to CSV file
@app.route('/export', methods=['GET'])
def export_form_data():
    # get form data from database or any other storage

    # create a CSV file
    csv_file = open('form_data.csv', 'w', newline='')

    # create a CSV writer
    csv_writer = csv.writer(csv_file)

    # write header row
    csv_writer.writerow(['Name', 'Email', 'Phone'])

    # write form data rows
    for data in form_data:
        csv_writer.writerow([data['name'], data['email'], data['phone']])

    # close the CSV file
    csv_file.close()

    # return the CSV file as a download response
    response = make_response(csv_file)
    response.headers['Content-Disposition'] = 'attachment; filename=form_data.csv'
    response.headers['Content-Type'] = 'text/csv'

    return response

if __name__ == '__main__':
    app.run(debug=True)
