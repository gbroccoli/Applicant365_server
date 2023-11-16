from typing import NamedTuple

# Модель для описания словарей, включенных в список статических файлов
# Model for describing dictionaries included in the list of static files
class StaticType(NamedTuple):
    subpath: str
    dir: str
    name: str