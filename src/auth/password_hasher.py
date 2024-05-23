import bcrypt

class PasswordHasher:
    def hash_password(self, password):
        raise NotImplementedError

    def check_password(self, stored_password, provided_password):
        raise NotImplementedError

class BcryptPasswordHasher(PasswordHasher):
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, stored_password, provided_password):
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))
