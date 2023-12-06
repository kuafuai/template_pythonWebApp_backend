from flask import Flask, request
from app.models import Config, AppConfig

app = Flask(__name__)

@app.route('/config_create', methods=['POST'])
def config_create():
    parent_id = request.form.get('parent_id')
    key = request.form.get('key')
    value = request.form.get('value')
    status = request.form.get('status')
    config_id = Config.create(parent_id, key, value, status)
    return str(config_id)

@app.route('/config_update', methods=['POST'])
def config_update():
    id = request.form.get('id')
    value = request.form.get('value')
    updated_config_id = Config.update(id, value)
    return str(updated_config_id)

@app.route('/config_status_update', methods=['POST'])
def config_status_update():
    id = request.form.get('id')
    status = request.form.get('status')
    updated_config_id = Config.update_status(id, status)
    return str(updated_config_id)

@app.route('/app_config_create', methods=['POST'])
def app_config_create():
    value = request.form.get('value')
    app_id = AppConfig.create(value)
    return str(app_id)

@app.route('/get_value', methods=['GET'])
def get_value():
    app_code = request.args.get('app_code')
    key = request.args.get('key')
    result = Config.get_value(app_code, key)
    return result

if __name__ == '__main__':
    app.run()
