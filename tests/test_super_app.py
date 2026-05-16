import unittest

from super_app import Student, Teacher, User


class TestSuperApp(unittest.TestCase):
    def test_user_login_sets_logged_in(self):
        user = User("Avery")
        self.assertFalse(user.logged_in)

        result = user.log_in()

        self.assertTrue(user.logged_in)
        self.assertEqual(result, "Avery is now logged in.")

    def test_student_init_inherits_user_name(self):
        student = Student("Jordan", 10)

        self.assertEqual(student.name, "Jordan")
        self.assertEqual(student.grade, 10)
        self.assertFalse(student.logged_in)
        self.assertFalse(student.in_class)

    def test_student_login_calls_super_and_sets_in_class(self):
        student = Student("Jordan", 10)
        result = student.log_in()

        self.assertTrue(student.logged_in)
        self.assertTrue(student.in_class)
        self.assertEqual(result, "Jordan (grade 10) is logged in and in class.")

    def test_teacher_login_inherits_user_login(self):
        teacher = Teacher("Morgan", "History")

        self.assertFalse(teacher.logged_in)
        result = teacher.log_in()

        self.assertTrue(teacher.logged_in)
        self.assertEqual(result, "Morgan (teacher of History) is now logged in.")

    def test_teacher_does_not_have_in_class(self):
        teacher = Teacher("Morgan", "History")
        self.assertFalse(hasattr(teacher, "in_class"))


if __name__ == "__main__":
    unittest.main()
