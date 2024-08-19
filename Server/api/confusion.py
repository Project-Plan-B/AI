from flask import Blueprint, request

bp = Blueprint("confusion", __name__, url_prefix='/confusion')
confusion = {"A": 1, "B": 3, "C": 1, "D": 3, "E": 4, "F": 3}  # confusion level
level = '12233444'


# 카메라에서 혼잡도 받기
@bp.route('/info', methods=["POST"])
def info_confusion():
    global confusion
    if request.method == "POST":
        data = request.get_json()['list']
        confu = {k: level[v] for k, v in zip("ABCDEF", data)}
        confusion = confu
        return {"message": "혼잡도 정보가 갱신되었습니다."}, 201
    return {"error": "요청이 잘못되었습니다."}, 405


# 앱으로 혼잡도 보내기
@bp.route('/send', methods=['GET'])
def send_confusion():
    return confusion, 200
