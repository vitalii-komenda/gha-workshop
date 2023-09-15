import unittest
from api import app
from repositories.tasks import create_task, get_task_by_id, delete_task, update_task, get_tasks, db, init_app


class DatabaseRepositoryTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app.config.from_object('config.TestingConfig')

        with self.app.app_context():
            init_app(self.app)  # Ensure that init_app is called
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_and_get_task(self):
        with self.app.app_context():
            new_task = create_task(
                {'name': 'Test Task', 'description': 'Test Description'})
            task = get_task_by_id(new_task.id)
            self.assertIsNotNone(task)
            self.assertEqual(task.name, 'Test Task')
            self.assertEqual(task.description, 'Test Description')

    def test_get_tasks(self):
        with self.app.app_context():
            # Creating multiple tasks
            create_task({'name': 'Task 1', 'description': 'Description 1'})
            create_task({'name': 'Task 2', 'description': 'Description 2'})

            # Getting all tasks
            tasks = get_tasks()
            self.assertEqual(len(tasks), 2)
            self.assertEqual(tasks[0].name, 'Task 1')
            self.assertEqual(tasks[1].name, 'Task 2')

    def test_update_task(self):
        with self.app.app_context():
            # Creating a task to update
            task = create_task(
                {'name': 'Task 1', 'description': 'Description 1'})

            # Updating the task
            update_task(task.id, {'name': 'Updated Task',
                        'description': 'Updated Description'})

            # Getting the updated task
            updated_task = get_task_by_id(task.id)
            self.assertEqual(updated_task.name, 'Updated Task')
            self.assertEqual(updated_task.description, 'Updated Description')

    def test_delete_task(self):
        with self.app.app_context():
            # Creating a task to delete
            task = create_task(
                {'name': 'Task 1', 'description': 'Description 1'})

            # Deleting the task
            delete_task(task.id)

            # Trying to get the deleted task
            deleted_task = get_task_by_id(task.id)
            self.assertIsNone(deleted_task)
# ... (you would add more test methods here to test other functionalities)


if __name__ == '__main__':
    unittest.main()
