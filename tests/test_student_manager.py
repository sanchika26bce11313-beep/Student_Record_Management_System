import unittest
import tempfile
import os
import json

from src.student_manager import StudentManager
from src import storage


class TestStudentManager(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()
        self.original_file = storage.DATA_FILE
        storage.DATA_FILE = self.temp_file.name

        with open(storage.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)

        self.manager = StudentManager()

    def tearDown(self):
        storage.DATA_FILE = self.original_file
        os.unlink(self.temp_file.name)

    def sample(self, student_id="1"):
        return {
            "id": student_id,
            "name": "Aarav",
            "age": 19,
            "course": "Python",
            "marks": 85
        }

    def test_add_and_search(self):
        self.assertTrue(self.manager.add_student(self.sample()))
        self.assertIsNotNone(self.manager.search_student("1"))

    def test_duplicate_id(self):
        self.assertTrue(self.manager.add_student(self.sample()))
        self.assertFalse(self.manager.add_student(self.sample()))

    def test_update(self):
        self.manager.add_student(self.sample())
        updated = self.sample()
        updated["marks"] = 95
        self.assertTrue(self.manager.update_student("1", updated))
        self.assertEqual(self.manager.search_student("1")["marks"], 95.0)

    def test_delete(self):
        self.manager.add_student(self.sample())
        self.assertTrue(self.manager.delete_student("1"))
        self.assertIsNone(self.manager.search_student("1"))

    def test_report(self):
        self.manager.add_student(self.sample("1"))
        second = self.sample("2")
        second["marks"] = 95
        self.manager.add_student(second)
        report = self.manager.generate_report()
        self.assertEqual(report["total"], 2)
        self.assertEqual(report["average_marks"], 90.0)


if __name__ == "__main__":
    unittest.main()
