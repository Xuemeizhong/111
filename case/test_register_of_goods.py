#encoding: utf-8
import pytest
import allure

from common.tools import yaml_replace_for_filter
from service.register_of_goods import RegisterOfGoodsService
from service.arn_manager import ArnManagerService
from common.logger import logger
import random

@allure.feature('按货品收获登记')
class TestRegisterOfGoods:

    @allure.title('获取ARN单中可收货登记列表数据')
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True) #登录依赖测试案例
    @pytest.mark.parametrize("data", yaml_replace_for_filter('arn_search.yml',dir_case='receive_good', filter='search_list')) 
    def test_Arn_Search(self,login,data):
        """根据ARN单查询"""
        result = RegisterOfGoodsService.arn_search_list(data)
        assert result.status_code == 200
        assert result.json()['code'] == 1

    @allure.title('根据ARN单号获取数据')
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True) #登录依赖测试案例
    @pytest.mark.parametrize("search_data", yaml_replace_for_filter('arn_search.yml',dir_case='receive_good', filter='search_list'))
    @pytest.mark.parametrize("receive_data", yaml_replace_for_filter('arn.yml',dir_case='arn', filter='query',index=1))
    def test_arn_receive(self,login,search_data,receive_data):
        """根据ARN单查询"""
        search_list = RegisterOfGoodsService.arn_search_list(search_data)
        index =random.randint(0,20)
        
        #更新arnCode值为ARn列表中的值
        receive_data['data']['arnCode']=search_list.json()["data"]["list"][index]["arnCode"]
        
        result = ArnManagerService.arn_query(receive_data)
        assert result.status_code == 200
        
        assert result.json()['code'] == 1

    @allure.title('根据ARN单号获取数据-无效ARN单号')
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True) #登录依赖测试案例
    @pytest.mark.parametrize("data", yaml_replace_for_filter('arn_search.yml',dir_case='receive_good', filter='arn_receive',index=2))
    def test_Arn_receive_of_invalid(self,login,data):
        """根据ARN单查询"""
        result = RegisterOfGoodsService.arn_search_list(data)
        assert result.status_code == 200
        assert result.json()['code'] == 1