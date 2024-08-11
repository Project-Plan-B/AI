from flask import Blueprint, request
from Server.database.model import Room

bp = Blueprint('alert', __name__)


@bp.route('/alert/<int:room_id>', methods=["GET"])
def show_alert(room_id):
    if request.method == "GET":
        data = Room.query.filter(Room.id == room_id).first()
        if not data:
            return {"error": "해당 데이터가 없습니다."}, 400
        floor = data.floor
        name = data.name
        confu = data.confusion
        return {"room_floor": floor, "room_name": name, "room_confusion": confu}, 200
    return {"error": "요청이 잘못되었습니다."}, 405
