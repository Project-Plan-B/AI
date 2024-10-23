from flask import Blueprint, request
from Server.database.model import db, Room

bp = Blueprint("confusion", __name__, url_prefix='/confusion')
confusion = {"A": 1, "B": 2, "C": 1, "D": 3, "E": 4, "F": 3}  # confusion level
level = '1223344'


# 카메라에서 혼잡도 받기
@bp.route('/info', methods=["POST"])
def info_confusion():
    global confusion
    if request.method == "POST":
        data = request.get_json()['list']
        confu = {k: int(level[v]) for k, v in zip("ABCDEF", data)}
        # 혼잡도 DB 갱신 필요
        confusion = confu
        total = sum(data) // 6
        db.session.query(Room).filter(Room.name == "test").update({"confusion": level[total]})
        db.session.commit()
        return {"message": "혼잡도 정보가 갱신되었습니다."}, 201
    return {"error": "요청이 잘못되었습니다."}, 405


# 앱으로 혼잡도 보내기
@bp.route('/send', methods=['GET'])
def send_confusion():
    return confusion, 200
