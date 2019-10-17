#encoding: utf-8

import allure
import  pytest
from common.tools import yaml_replace_for_filter

@allure.feature('登录模块')
@allure.tag('登录PDA')
class TestLogin:
    
    @allure.title('登录功能')
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)
    def test_login_success(self,login):
        '''
            登录接口测试案例
        :return:
        '''
        assert  login.status_code == 200
        assert login.json()['code'] ==1



