from flask_migrate import Migrate
from models.task import Task, db
from flask_sqlalchemy import SQLAlchemy


def init_app(app):
    if not db._app_engines:
        db.init_app(app)
        migrate = Migrate(app, db)


def get_tasks():
    return Task.query.all()


def create_task(task_data):
    new_task = Task(name=task_data['name'],
                    description=task_data.get('description'))
    db.session.add(new_task)
    db.session.commit()
    return new_task


def get_task_by_id(task_id):
    return Task.query.filter_by(id=task_id).first()


def update_task(task_id, update_data):
    task = get_task_by_id(task_id)
    if task:
        task.name = update_data.get('name', task.name)
        task.description = update_data.get('description', task.description)
        db.session.commit()
    return task


def delete_task(task_id):
    task = get_task_by_id(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return task
