from flask import Blueprint, request
from Server.database.model import Room

bp = Blueprint('alert', __name__)


@bp.route('/alert/<int:room_id>', methods=["GET", "POST"])
def show_alert(room_id):
    if request.method == "POST":
        want_confu = request.get_json()['want_confusion']
        data = Room.query.filter(Room.id == room_id).first()
        if not data:
            return {"error": "해당 데이터가 없습니다."}, 400
        floor = data.floor
        name = data.name
        confusion = data.confusion
        print(confusion, want_confu)
        if confusion == want_confu:
            return {"message": "현재 자습실이 원하는 혼잡도 상태가 되었습니다."}, 200
        return {"room_floor": floor, "room_name": name, "want_confusion": want_confu}, 201
    return {"error": "요청이 잘못되었습니다."}, 405
