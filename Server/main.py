from flask import Flask, request, jsonify

app = Flask(__name__)
temperature, humidity, co2 = 0, 0, 0  # DB로 옮길 예정


# 온도, 습도, co2 농도
@app.route('/info/other', methods=["GET", "POST"])
def info_other():
    global temperature, humidity, co2
    if request.method == "POST":
        data = request.get_json()
        if not data:
            return {"error": "정보가 잘못되었습니다"}, 400
        temperature = data['temperature']
        humidity = data['humidity']
        co2 = data['co2']
        return jsonify({'temperature': temperature, 'humidity': humidity, 'co2': co2}), 201
    else:
        return {"error": "오류가 발생했습니다"}, 400


# lidar 정보 (소켓 사용 예정)
# @app.route('/info/lidar', methods=["GET", "POST"])
# def info_lidar():
#     if request.method == "POST":
#         data = request.json.get()


# 앱으로 온도, 습도, co2 농도 보내기
@app.route('/send/other', methods=["get"])
def send_other():
    return jsonify({'temperature': temperature, 'humidity': humidity, 'co2': co2}), 201


# 앱으로 혼잡도 보내기
@app.route('/send/confusion', methods=['GET'])
def send_confusion():
    confusion = 0
    # ai 이용
    return jsonify({'confusion': confusion})
