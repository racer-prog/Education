from unittest import TestCase


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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.keys():
            print(cls.all_results[i])

    def test_1(self):
        self.obj_1 = Tournament(90,self.runner_1,self.runner_3)
        result_1 = self.obj_1.start()
        dict_ = {}
        for i in result_1.keys():
            dict_[i] = str(result_1[i])
        self.all_results["test1"] = dict_
        # print(list(dict_.items())[-1][1])
        self.assertTrue(list(dict_.items())[-1][1],"Ник")


    def test_2(self):
        self.obj_2 = Tournament(90,self.runner_2,self.runner_3)
        result_2 = self.obj_2.start()
        dict_ = {}
        for i in result_2.keys():
            dict_[i] = str(result_2[i])
        self.all_results["test2"] = dict_
        # print(list(dict_.items())[-1][1])
        self.assertTrue(list(dict_.items())[-1][1], "Ник")


    def test_3(self):
        self.obj_3 = Tournament(90,self.runner_1,self.runner_2,self.runner_3)
        result_3 = self.obj_3.start()
        dict_ = {}
        for i in result_3.keys():
            dict_[i] = str(result_3[i])
        self.all_results["test3"] = dict_
        # print(list(dict_.items())[-1][1])
        self.assertTrue(list(dict_.items())[-1][1], "Ник")




