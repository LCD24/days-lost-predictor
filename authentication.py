from connection_factory import get_connection
from functools import wraps
from flask import jsonify

def check_auth(username, password):
    connection = get_connection()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        return result is not None
    
def authenticate():
    return jsonify({"message": "Authentication required"}), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}

    
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated