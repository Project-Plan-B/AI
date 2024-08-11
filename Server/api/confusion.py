from flask import Blueprint, jsonify

bp = Blueprint("confusion", __name__, url_prefix='/confusion')
confusion = {"A": 2, "B": 3, "C": 1, "D": 2, "E": 4, "F": 3}  # confusion level


# 앱으로 혼잡도 보내기
@bp.route('', methods=['GET'])
def send_confusion():
    # ai 이용
    return jsonify(confusion), 200
