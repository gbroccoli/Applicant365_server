from config import EnvVariables

env = EnvVariables()

class PasswordManager:
    @staticmethod
    def hash_password(password):