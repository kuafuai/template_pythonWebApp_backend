from flask import request, jsonify
from app import app, db
from app.models import Demo

# 添加用户
@app.route('/demos', methods=['POST'])
def add_demo():
    data = request.get_json()
    new_demo = Demo(info1=data['info1'], info2=data['info2'])
    db.session.add(new_demo)
    db.session.commit()
    return jsonify({'message': 'Demo added successfully'})

# 获取所有用户
@app.route('/demos', methods=['GET'])
def get_demos():
    demos = Demo.query.all()
    demo_list = []
    for demo in demos:
        demo_data = {'id': demo.id, 'info1': demo.info1, 'info2': demo.info2}
        demo_list.append(demo_data)
    return jsonify({'demos': demo_list})

# 获取单个用户
@app.route('/demos/<int:demo_id>', methods=['GET'])
def get_demo(demo_id):
    demo = Demo.query.get(demo_id)
    if demo:
        demo_data = {'id': demo.id, 'info1': demo.info1, 'info2': demo.info2}
        return jsonify(demo_data)
    return jsonify({'message': 'Demo not found'}), 404

# 更新用户信息
@app.route('/demos/<int:demo_id>', methods=['PUT'])
def update_demo(demo_id):
    demo = Demo.query.get(demo_id)
    if not demo:
        return jsonify({'message': 'Demo not found'}), 404

    data = request.get_json()
    demo.info1 = data['info1']
    demo.info2 = data['info2']
    db.session.commit()
    return jsonify({'message': 'Demo updated successfully'})

# 删除用户
@app.route('/demos/<int:demo_id>', methods=['DELETE'])
def delete_demo(demo_id):
    demo = Demo.query.get(demo_id)
    if not demo:
        return jsonify({'message': 'Demo not found'}), 404

    db.session.delete(demo)
    db.session.commit()
    return jsonify({'message': 'Demo deleted successfully'})
