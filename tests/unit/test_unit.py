import unittest
from todoapp.models import Task, User


class TestAssertWorks(unittest.TestCase):

    def setUp(self):
        user = User.objects.create(username="sampath", password="sampath")
        Task.objects.create(task_name="1st_Task",
                          task_description="This is first task",
                          task_status=0, task_priority=1, task_visibility=1,
                          user_name=user)

    def test_check_task_save(self):
        task = Task.objects.filter(task_name="1st_Task")
        self.assertEqual(len(task), 1, "task was not saved")

    def test_status_for_all_tasks(self):
        resp = self.client().get('/tasks')
        self.assertEqual(resp.status_code, 200, "tasks are not retrieving")

