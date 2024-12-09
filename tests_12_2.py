from unittest import TestCase

from nuitka.nodes.shapes.BuiltinTypeShapes import pow_shapes_set


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

    def setUpClass(self):
        self.all_results = {}


    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)



    def tearDownClass(self):
        for key in self.all_results.keys():
            print(self.all_results[key])

    def test_1(self):
        self.obj_1 = Tournament(90,self.runner_1,self.runner_3)
        result = self.obj_1.start()
        self.all_results.update(result)




