# This code is importing the `listdir` function from the `os` module and the `import_module` function
# from the `importlib` module.
from os import listdir
from importlib import import_module

urls = []

path_routers = "routers"

# Получаем список файлов роутеров
routers_file = [file for file in listdir(path_routers) if file.endswith(".py") and file != "__init__.py"]

# Проходим по каждому файлу роутера
for router in routers_file:
    # Формируем имя модуля на основе имени файла
    module_name = "routers.{}".format(router[:-3])
    
    # Загружаем модуль
    module = import_module(module_name)

    # Проверяем наличие атрибута 'routers' в модуле
    if hasattr(module, "routers"):
        # Если атрибут существует, добавляем его содержимое в список 'urls'
        urls.extend(module.routers)