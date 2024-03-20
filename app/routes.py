from flask import Flask, jsonify, request
import itchat

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    itchat.auto_login()
    return jsonify({'status': 'success', 'message': 'Login successful'})

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    username = data.get('username')
    message = data.get('message')
    itchat.send(message, toUserName=username)
    return jsonify({'status': 'success', 'message': 'Message sent'})

@app.route('/get_contact_list', methods=['GET'])
def get_contact_list():
    contact_list = itchat.get_contact()
    return jsonify({'status': 'success', 'contact_list': contact_list})

@app.route('/add_friend', methods=['POST'])
def add_friend():
    data = request.get_json()
    username = data.get('username')
    itchat.add_friend(userName=username)
    return jsonify({'status': 'success', 'message': 'Friend added'})

@app.route('/get_user_profile', methods=['GET'])
def get_user_profile():
    user_profile = itchat.search_friends()
    return jsonify({'status': 'success', 'user_profile': user_profile})

@app.route('/update_user_profile', methods=['POST'])
def update_user_profile():
    data = request.get_json()
    username = data.get('username')
    nickname = data.get('nickname')
    itchat.update_friend(userName=username, nickName=nickname)
    return jsonify({'status': 'success', 'message': 'Profile updated'})

if __name__ == '__main__':
    app.run()
