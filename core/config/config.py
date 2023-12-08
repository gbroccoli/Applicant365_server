from dotenv import dotenv_values
from typing import NamedTuple

class Urls(NamedTuple):
	address: str
	port: int

class EnvVariables:
	def __init__(self, file_path=".env"):
		self.file_path = file_path
		self.variables = self.load_variables()

	def load_variables(self):
		return dotenv_values(self.file_path)

	def get_value(self, key, *, default=None):
		value = self.variables.get(key)
		return value if value is not None and value != '' else default
	
	def get_params_local_url(self) -> Urls:
		local_url = self.get_value("APP_URL", default="localhost:8000")
		
		if "://" in local_url:
			local_url = local_url.split("://")[1]
		
		address, port_str = local_url.split(":")
		port = int(port_str)

		return Urls(address=address, port=port)