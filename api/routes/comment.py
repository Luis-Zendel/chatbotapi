from flask import Blueprint
import db
comment_bp = Blueprint('comments',__name__ )

@comment_bp.route('/get', methods = ['GET'])
def obtenerComentarios():
    return "hello"