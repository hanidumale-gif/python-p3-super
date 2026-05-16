class User:
    def __init__(self, name):
        self.name = name
        self.logged_in = False

    def log_in(self):
        self.logged_in = True
        return f"{self.name} is now logged in."


class Student(User):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade
        self.in_class = False

    def log_in(self):
        super().log_in()
        self.in_class = True
        return f"{self.name} (grade {self.grade}) is logged in and in class."


class Teacher(User):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def log_in(self):
        super().log_in()
        return f"{self.name} (teacher of {self.subject}) is now logged in."
