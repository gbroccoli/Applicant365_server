from typing import NamedTuple
from envdatareader import EnvDataReader


class Urls(NamedTuple):
    address: str
    port: int


class EnvVariables(EnvDataReader):

    def get_params_local_url(self) -> Urls:
        local_url = self.get_value("APP_URL", default="localhost:8000")

        if "://" in local_url:
            local_url = local_url.split("://")[1]

        address, port_str = local_url.split(":")
        port = int(port_str)

        return Urls(address=address, port=port)
