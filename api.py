from flask import Flask, request, jsonify
import os
from repositories.tasks import get_tasks, create_task, get_task_by_id, update_task, delete_task, init_app, db

app = Flask(__name__)
env_config = os.getenv("FLASK_ENV", "default")

if env_config == "production":
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

init_app(app)
with app.app_context():
    db.create_all()


@app.route('/tasks', methods=['GET'])
def get_tasks_route():
    return jsonify(get_tasks())


@app.route('/tasks', methods=['POST'])
def create_task_route():
    new_task = request.get_json()
    return jsonify(create_task(new_task)), 201


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_route(task_id):
    task = get_task_by_id(task_id)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task_route(task_id):
    update_data = request.get_json()
    task = update_task(task_id, update_data)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task)


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_route(task_id):
    delete_task(task_id)
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0')
