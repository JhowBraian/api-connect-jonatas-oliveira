# routes/user_routes.py
from flask import Blueprint, request, jsonify
from models.user_model import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user_by_id,
    delete_user_by_id
)

user_bp = Blueprint('user_bp', __name__)

# 1. Listagem geral de usuários (GET /api/users)
@user_bp.route('/api/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify({
        "data": users,
        "status": "sucesso"
    }), 200

# 2. Busca de usuário por ID (GET /api/users/)
@user_bp.route('/api/users/', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({
            "error": f"Usuário com ID {user_id} não encontrado.",
            "status": "erro"
        }), 404
    return jsonify({
        "data": user,
        "status": "sucesso"
    }), 200

# 3. Criação de usuário (POST /api/users)
@user_bp.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or not data.get('nome') or not data.get('email'):
        return jsonify({
            "error": "Os campos 'nome' e 'email' são obrigatórios.",
            "status": "erro"
        }), 400

    novo_usuario = create_user(
        nome=data.get('nome'),
        email=data.get('email')
    )
    return jsonify({
        "data": novo_usuario,
        "status": "sucesso"
    }), 201

# 4. Atualização de usuário (PUT /api/users/)
@user_bp.route('/api/users/', methods=['PUT'])
def edit_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({
            "error": f"Usuário com ID {user_id} não encontrado.",
            "status": "erro"
        }), 404

    data = request.get_json()
    if not data:
        return jsonify({
            "error": "Dados inválidos para atualização.",
            "status": "erro"
        }), 400

    usuario_atualizado = update_user_by_id(
        user_id=user_id,
        nome=data.get('nome'),
        email=data.get('email')
    )
    return jsonify({
        "data": usuario_atualizado,
        "status": "sucesso"
    }), 200

# 5. Remoção de usuário (DELETE /api/users/)
@user_bp.route('/api/users/', methods=['DELETE'])
def remove_user(user_id):
    removido = delete_user_by_id(user_id)
    if not removido:
        return jsonify({
            "error": f"Usuário com ID {user_id} não encontrado.",
            "status": "erro"
        }), 404

    return jsonify({
        "mensagem": f"Usuário com ID {user_id} removido com sucesso.",
        "status": "sucesso"
    }), 200
