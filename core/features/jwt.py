from jose import jwt
from datetime import datetime, timedelta
from envdatareader import EnvDataReader


class Token:

    @classmethod
    def create(cls, data: dict, remember: bool):
        to_encode = data.copy()

        if remember:
            expire = datetime.utcnow() + timedelta(days=30)
        else:
            expire = datetime.utcnow() + timedelta(hours=2)

        # Преобразуйте объект datetime в строку в формате ISO
        expire_str = expire.isoformat()
        to_encode.update({"token": expire_str})

        encoded_jwt = jwt.encode(to_encode, EnvDataReader().get_value(
            "APP_KEY"), EnvDataReader().get_value("APP_ALGORITHM"))

        return encoded_jwt
