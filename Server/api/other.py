from flask import Blueprint, jsonify, request

bp = Blueprint('other', __name__, url_prefix='/other')
temperature, humidity = 0, 0


# 온도, 습도, co2 농도
@bp.route('/info', methods=["GET", "POST"])
def info_other():
    global temperature, humidity
    if request.method == "POST":
        data = request.get_json()
        key = [d for d in data.keys() if d != 'temperature' and d != 'humidity']
        if (not data) or key:
            return {"error": "정보가 잘못되었습니다"}, 400
        temperature = data['temperature']
        humidity = data['humidity']
        return jsonify({'temperature': temperature, 'humidity': humidity}), 201
    else:
        return {"error": "오류가 발생했습니다"}, 400


# 앱으로 온도, 습도, co2 농도 보내기
@bp.route('/send', methods=["get"])
def send_other():
    return jsonify({'temperature': temperature, 'humidity': humidity}), 201
