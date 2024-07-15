from functools import wraps
from flask import request, jsonify
from connection_factory import get_connection, get_oracle_connection

def find_by_username(username):
    connection = get_oracle_connection()
    with connection.cursor() as cursor:
        query = "SELECT * FROM users WHERE username=:1"
        cursor.execute(query, (username,))
        return cursor.fetchone()

class Authenticator:
    def __init__(self, password_hasher):
        self.password_hasher = password_hasher

    def check_auth(self, username, password):
        user = find_by_username(username)
        return user and self.password_hasher.check_password(user[2], password)

    def authenticate(self, message):
        return jsonify({"message": message}), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}

    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if not auth:
                return self.authenticate("Authentication required")
            elif not self.check_auth(auth.username, auth.password):
                return self.authenticate("Invalid authentication")
            return f(*args, **kwargs)
        return decorated
