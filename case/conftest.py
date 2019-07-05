#encoding:utf-8
import pytest





@pytest.fixture(scope='class')
def acress_web():
    print('这是一条前置操作')
    yield
    print('这是一条后置操作后的最终操作')

@pytest.fixture
def refresh_web():
    yield
    print('这是一条后置操作')