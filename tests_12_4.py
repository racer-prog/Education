from unittest import TestCase
import unittest
import logging


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class RunnerTest(TestCase):

    is_frozen = True

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
            try:
                self.obj_test1 = Runner("Name1",-5)

                if self.obj_test1.speed < 0:
                    raise ValueError (f"Скорость не может быть меньше нуля, сейчас {self.obj_test1.speed}")
                for i in range(10):
                    self.obj_test1.walk()
                self.assertEqual(self.obj_test1.distance, 50, "Should be 50")
                logging.info('"test_walk" выполнен успешно')
            except ValueError as v_err:
                logging.warning(f"Неверная скорость для Runner. {v_err}", exc_info=True)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            self.obj_test2 = Runner(2)
            if type(self.obj_test2.name) != str:
                raise TypeError(f"Имя может быть только строкой, сейчас: {type(self.obj_test2.name).__name__}")
            for i in range(10):
                self.obj_test2.run()
            self.assertEqual(self.obj_test2.distance, 100, "Should be 100")
        except TypeError as t_err:
            logging.warning(f"Неверное имя для Runner. {t_err}", exc_info=True)

    @unittest.skipUnless(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):

        self.obj_test3 = Runner("Name3")
        self.obj_test4 = Runner("Name4")
        for i in range(10):
            self.obj_test3.run()
            self.obj_test4.walk()
        self.assertNotEqual(self.obj_test3.distance, self.obj_test4.distance, "Should be different")



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="runner_tests.log",
                        filemode="w", encoding="UTF-8",
                        format="%(levelname)s -> %(message)s")

