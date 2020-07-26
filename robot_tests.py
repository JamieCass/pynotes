import unittest
from robot import Robot


class RobotTests(unittest.TestCase):

    def setUp(self): # we setup a robot called Mega Man and then we can use this robot in every test below
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self): # a test that will check if charge will make batery 100%
        """Testing to see if the charge function will recharge battery to 100%"""
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self): # a test that will check if say name comes back with 'BEEP BOOP, etc.....'
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()
