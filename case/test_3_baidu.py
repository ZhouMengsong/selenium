import pytest
import time



@pytest.mark.usefixtures('acress_web')
class TestBaidu():

    @pytest.mark.somke
    def test_dome(self,):
        print('hello word')
        time.sleep(2)

