import requests

retorno = requests.get("http://127.0.0.1:8000/teste/1")
print(retorno.json())