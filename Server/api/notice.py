from Server.database.model import Alert, db
from flask import Blueprint, jsonify, request

bp = Blueprint('notice', __name__, url_prefix='/list')


@bp.route('/create', methods=['GET', 'POST'])
def add_alert():
    if request.method == "POST":
        data = request.get_json()
        key = [i for i in data.keys() if i != 'title' and i != 'content']
        if (not data) or key:
            return {"error": "정보가 잘못되었습니다."}, 400
        a = Alert()
        a.title = data['title']
        a.content = data['content']
        db.session.add(a)
        db.session.commit()
        return jsonify({"success": "공지사항이 만들어졌습니다."}), 201
    return {"error": "요청이 잘못되었습니다."}, 405


@bp.route('/cancel/<int:post_id>', methods=["POST"])
def delete_alert(post_id):
    if request.method == "POST":
        Alert.query.filter(Alert.id == post_id).delete()
        Alert.commit()
        return {"success": "성공적으로 삭제되었습니다."}, 204
    return {"error": "요청이 잘못되었습니다."}, 405


@bp.route('/show_all', methods=["GET"])
def show_alert():
    if request.method == "GET":
        results = Alert.query.order_by(Alert.id.desc()).all()
        return {"list": [
            {"post_id": result.id, "title": result.title, "writing": result.writing} for result in results]
        }, 200
    return {"error": "요청이 잘못되었습니다."}, 405


@bp.route('/show/<int:post_id>', methods=["GET"])
def show_alert_id(post_id):
    if request.method == "GET":
        result = Alert.query.filter(Alert.id == post_id).first()
        return {"content": result.content}, 200
    return {"error": "요청이 잘못되었습니다."}, 405
