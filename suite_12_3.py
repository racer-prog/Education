import unittest
import tests_12_2 as test_t
import tests_12_1 as test_r


myST = unittest.TestSuite()
myST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_t.TournamentTest))
myST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_r.RunnerTest))

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(myST)



