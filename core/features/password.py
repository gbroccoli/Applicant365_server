from .mainclass import Validation
import re


class ValidationPassword(Validation):

    @classmethod
    def is_valid_password(cls, password: str):
        # Example: Password should contain at least 8 characters, one digit,
        # one uppercase and lowercase letter, and one special character
        pattern = (
            r'^(?=.*\d)'          # at least one digit
            r'(?=.*[a-z])'        # at least one lowercase letter
            r'(?=.*[A-Z])'        # at least one uppercase letter
            r'(?=.*[!@#$%^&*()_+}{":;\'])'  # at least one special character
            r'(?=.*[a-zA-Z])'     # at least one letter (optional)
            r'.{8,}$'             # at least 8 characters
        )
        return re.match(pattern, password) is not None
