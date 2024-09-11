import requests

base_url = "https://demoqa.com"

def create_user(username, password):
    url = f"{base_url}/Account/v1/User"
    payload = {
        "userName": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    print(f"Status de criação do usuário: {response.status_code}")
    print(f"Resposta da API (Criação de Usuário): {response.json()}")
    return response.json()

def generate_token(username, password):
    url = f"{base_url}/Account/v1/GenerateToken"
    payload = {
        "userName": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    print(f"Status de geração de token: {response.status_code}")
    print(f"Resposta da API (Geração de Token): {response.json()}")
    return response.json()

def confirm_authorization(username, password):
    url = f"{base_url}/Account/v1/Authorized"
    payload = {
        "userName": username,
        "password": password
    }
    response = requests.post(url, json=payload)
    print(f"Status de autorização: {response.status_code}")
    print(f"Resposta da API (Autorização): {response.json()}")
    return response.json()

def list_books():
    url = f"{base_url}/BookStore/v1/Books"
    response = requests.get(url)
    print(f"Status de listagem de livros: {response.status_code}")
    print(f"Resposta da API (Livros Disponíveis): {response.json()}")
    return response.json()

def rent_books(user_id, book_ids, token):
    url = f"{base_url}/BookStore/v1/Books"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "userId": user_id,
        "collectionOfIsbns": [{"isbn": book_id} for book_id in book_ids]
    }
    response = requests.post(url, json=payload, headers=headers)
    print(f"Status de aluguel de livros: {response.status_code}")
    print(f"Resposta da API (Aluguel de Livros): {response.json()}")
    return response.json()

def get_user_details(user_id, token):
    url = f"{base_url}/Account/v1/User/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(f"Status de listagem de detalhes do usuário: {response.status_code}")
    print(f"Resposta da API (Detalhes do Usuário): {response.json()}")
    return response.json()

username = "testeQA2"
password = "Teste@123"

user_response = create_user(username, password)
if 'userID' in user_response:
    user_id = user_response['userID']
else:
    print("Erro na criação do usuário. Verifique os logs.")
    exit()

token_response = generate_token(username, password)
if 'token' in token_response:
    token = token_response['token']
else:
    print("Erro na geração do token. Verifique os logs.")
    exit()

authorization_status = confirm_authorization(username, password)
if not authorization_status:
    print("Usuário não autorizado. Verifique os dados.")
    exit()

books = list_books()
if 'books' in books:
    print(f"Total de livros disponíveis: {len(books['books'])}")
    book_ids = [books['books'][0]['isbn'], books['books'][1]['isbn']]
else:
    print("Erro ao listar livros. Verifique os logs.")
    exit()

rent_response = rent_books(user_id, book_ids, token)

user_details = get_user_details(user_id, token)
