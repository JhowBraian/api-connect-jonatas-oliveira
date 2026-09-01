from flask import Flask, jsonify
from routes.user_routes import user_bp

app = Flask(__name__)

# Registro do Blueprint de rotas de usuário
app.register_blueprint(user_bp)

# Rota de status / verificação do servidor
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensagem": "Servidor da API Connect iniciado e operante!",
        "status": "sucesso"
    }), 200

if __name__ == '__main__':
    # Execução em 0.0.0.0 para aceitar conexões locais na porta 5000
    app.run(host='0.0.0.0', port=5000, debug=True)


