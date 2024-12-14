from flask import Blueprint, request, jsonify
from .models import db, User, Task

bp = Blueprint('routes', __name__)

# Rota para listar todas as tarefas
@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title, "status": t.status} for t in tasks])

# Rota para visualizar uma tarefa específica
@bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"id": task.id, "title": task.title, "status": task.status})

# Rota para criar uma nova tarefa
@bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(title=data['title'], user_id=data['user_id'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created!"}), 201

# Rota para atualizar uma tarefa existente
@bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    data = request.json
    task.title = data.get('title', task.title)
    task.status = data.get('status', task.status)
    db.session.commit()

    return jsonify({"message": "Task updated!", "task": {"id": task.id, "title": task.title, "status": task.status}})

# Rota para deletar uma tarefa
@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted!"})

# Função para registrar o blueprint
def register_routes(app):
    app.register_blueprint(bp)
