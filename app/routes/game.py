from flask import Blueprint, request

game_bp = Blueprint('game', __name__)

@game_bp.route('/update_direction', methods=['POST'])
def update_direction():
    direction = request.json.get('direction')
    # Update the player's direction based on the input
    # Your code here

    return 'Direction updated successfully'
