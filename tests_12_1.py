from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(TestCase):

    def test_walk(self):
        self.obj_test1 = Runner("Name1")
        for i in range(10):
            self.obj_test1.walk()
        self.assertEqual(self.obj_test1.distance, 50, "Should be 50")

    def test_run(self):

        self.obj_test2 = Runner("Name2")
        for i in range(10):
            self.obj_test2.run()
        self.assertEqual(self.obj_test2.distance, 100, "Should be 100")

    def test_challenge(self):
        self.obj_test3 = Runner("Name3")
        self.obj_test4 = Runner("Name4")
        for i in range(10):
            self.obj_test3.run()
            self.obj_test4.walk()
        self.assertNotEqual(self.obj_test3.distance, self.obj_test4.distance, "Should be different")



RunnerTest