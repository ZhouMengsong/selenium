import unittest

import configparser
class Test(unittest.TestCase):

    def test_one(self):
        '''test_one'''
        a=10
        b=10
        self.assertEqual(a,b)


if __name__ == '__main__':
    test = unittest.TestSuite()
    loader = unittest.TestLoader()
    test.addTest(loader.loadTestsFromTestCase(Test))
    t = unittest.TextTestRunner()
    t.run(test)