from flask import Blueprints, jsonify

bp = Blueprints("confusion", __name__, url_prefix='/confusion')


# 앱으로 혼잡도 보내기
@bp.route('/', methods=['GET'])
def send_confusion():
    confusion = 0
    # ai 이용
    return jsonify({'confusion': confusion})
