# encoding: utf-8


import pytest

from service.arn_manager import ArnManagerService
from common.tools import yaml_replace_for_filter
import allure




@allure.feature('ARN模块')
@allure.tag('ARN管理')
class TestArnManager:


    @allure.title('根据ARN单查询')
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True) #登录依赖测试案例
    @pytest.mark.parametrize("data", yaml_replace_for_filter('arn.yml',dir_case='arn', filter='query')) #当前测试接口依赖测试案例
    def test_arn_manager_query(self, login,data):
        """根据ARN单查询"""
        result = ArnManagerService.arn_query(data)
        assert result.status_code == 200
        assert result.json()['code'] == 0


    @allure.title('获取所有ARN单')
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)
    @pytest.mark.parametrize("data", yaml_replace_for_filter('arn.yml',dir_case='arn', filter='list'))
    def test_arn_manager_list(self,login,data):
        """根据仓库编码查询该仓库下的所有arn单"""
        result = ArnManagerService.arn_list(data)
        assert result.status_code == 200
        assert result.json()['code'] == 1

    @allure.title('ARN高级查询-条件组合查询')
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)  # 登录依赖测试案例
    @pytest.mark.parametrize("data", yaml_replace_for_filter('arn_filter.yml', dir_case='arn', filter='filter',index=2))  # 当前测试接口依赖测试案例
    def test_arn_manager_query_of_filter(self,login,data):
        result = ArnManagerService.arn_list(data)
        assert result.status_code == 200
        assert result.json()['code'] == 1

    @allure.title('ARN单可操作业务')
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)  # 登录依赖测试案例
    @pytest.mark.parametrize("data", yaml_replace_for_filter('arn.yml', dir_case='arn', filter='status'))
    def test_arn_manager_status(self,login,data):
        result = ArnManagerService.arn_sattus(data)
        assert result.status_code == 200
        assert result.json()['code'] == 1
    
if __name__ == "__main__":
    pytest.main(["-vs", "test_arn_manager.py"])
