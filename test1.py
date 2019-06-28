

import ddt

@ddt.ddt
class Test_print():
    '''test'''


    @ddt.data('a')
    def test_one(self,a):

        print(a)

if __name__ == '__main__':
    Test_print().test_one()