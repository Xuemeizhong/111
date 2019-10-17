#encoding: utf-8


import  pytest
import json
from common.send_all import SendRequest
import  allure

@allure.step('登录PDA')
@pytest.fixture(scope='function')
def login(request):
    return  SendRequest(request.param)
    #return Login.login_func(request.param)

