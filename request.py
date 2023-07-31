import requests

retorno = requests.post("http://127.0.0.1:8000/usuario", params={"id": 4, "nome": 'Bianca', "senha": "4"})
print(retorno.json())