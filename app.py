from flask import Flask
from app.database import init_db
from app.models import db  # Importando o db para configurar a conexão
from app.routes import register_routes
from flask import Flask, jsonify


app = Flask(__name__)

# Configurar o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///to_do_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar a conexão do banco de dados
init_db(app)

# Registrar as rotas
register_routes(app)

# Rota para a pagina inicial (raiz)
@app.route('/')
def home():
    return jsonify({"message": "Bem vindo a API de To-do-List!"})


if __name__ == "__main__":
    app.run(debug=True)
