import requests

# Endereço base da sua API C#
URL_BASE = "http://localhost:5041/api"

print("=== TESTANDO CONEXÃO PYTHON -> C# ===")

# 1. TESTANDO O GET (Listar Categorias)
print("\n1. Buscando categorias do arquivo JSON...")
resposta_get = requests.get(f"{URL_BASE}/categoria")

if resposta_get.status_code == 200:
    categorias = resposta_get.json()
    print("Sucesso! Dados recebidos do C#:")
    for cat in categorias:
        # Ajuste a chave de acordo com as propriedades da sua classe C# (Id, Descricao)
        print(f"-> ID: {cat.get('id')} | Descrição: {cat.get('descricao')}")
else:
    print(f"Erro ao buscar dados: {resposta_get.status_code}")


# 2. TESTANDO O POST (Inserir Categoria)
print("\n2. Tentando inserir uma nova categoria via Python...")
nova_cat = {"descricao": "Linha Gamer"}

# Enviamos o dicionário Python, o 'requests' converte automaticamente para o JSON que o C# espera
resposta_post = requests.post(f"{URL_BASE}/categoria", json=nova_cat)

if resposta_post.status_code in [200, 201]:
    print("Sucesso!", resposta_post.json())
else:
    print(f"Erro ao inserir: {resposta_post.status_code}", resposta_post.text)