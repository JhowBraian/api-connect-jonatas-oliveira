# models/user_model.py

# Estrutura de persistência em memória RAM
users_db = [
    {
        "id": 1,
        "nome": "Ana Silva",
        "email": "ana@email.com"
    },
    {
        "id": 2,
        "nome": "Carlos Souza",
        "email": "carlos@email.com"
    }
]

_next_id = 3

def get_all_users():
    """Retorna todos os usuários cadastrados."""
    return users_db

def get_user_by_id(user_id):
    """Localiza e retorna um usuário específico pelo ID."""
    return next((user for user in users_db if user["id"] == user_id), None)

def create_user(nome, email):
    """Cadastra um novo usuário com ID incremental único."""
    global _next_id
    new_user = {
        "id": _next_id,
        "nome": nome,
        "email": email
    }
    users_db.append(new_user)
    _next_id += 1
    return new_user

def update_user_by_id(user_id, nome=None, email=None):
    """Atualiza os dados de um usuário existente."""
    user = get_user_by_id(user_id)
    if not user:
        return None
    if nome is not None:
        user["nome"] = nome
    if email is not None:
        user["email"] = email
    return user

def delete_user_by_id(user_id):
    """Remove um usuário da lista em memória."""
    user = get_user_by_id(user_id)
    if not user:
        return False
    users_db.remove(user)
    return True
