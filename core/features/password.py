from .mainclass import Validation
import re

class ValidationPassword(Validation):

    @classmethod
    def is_valid_password(cls, password: str):
        # Пример: пароль должен содержать как минимум 8 символов, хотя бы одну цифру, одну букву в верхнем и нижнем регистре и один специальный символ
        return re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+}{":;\'])(?=.*[a-zA-Z]).{8,}$', password) is not None