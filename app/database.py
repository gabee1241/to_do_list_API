from flask_sqlalchemy import SQLAlchemy

# Criação da instância do banco de dados
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)  # Inicializando a conexão com o app
    with app.app_context():
        db.create_all()  # Cria as tabelas no banco

# Base para os modelos do SQLAlchemy
Base = db.Model  # Usando a classe db.Model como base para os modelos
