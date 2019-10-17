#encoding: utf-8

import pytest
import allure
from service.base import BaseInterService
from common.tools import yaml_replace_for_filter

@allure.feature('获取系统枚举')
class TestBase:

    @allure.title('获取任务类型')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum',index=1))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_WmsTaskType(self,login,data):
        
        result =BaseInterService.sys_enum(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取状态列表')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum',index=2))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_WmsArnStatus(self,login,data):
        result =BaseInterService.sys_enum(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取上架状态列表')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum',index=3))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_WmsArnShelvesStatus(self,login,data):
        result =BaseInterService.sys_enum(data)
        print(f"result_上架状态：{result.json()}")
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取物流类型')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum',index=4))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_ItemLogisticsType(self,login,data):
        result =BaseInterService.sys_enum(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取件型')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum',index=5))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_PieceType(self,login,data):
        result =BaseInterService.sys_enum(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取单位名称')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum',index=6))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_PackageUnitType(self,login,data):
        result =BaseInterService.sys_enum(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取单位级别')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum',index=7))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_PackageUnitLevel(self,login,data):
        result =BaseInterService.sys_enum(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('查询容器类型')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum',index=8))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_ConveyanceTypes(self,login,data):
        result =BaseInterService.sys_enum(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取获取委托方')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='current_org'))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_current_org(self,login,data):
        result =BaseInterService.current_org(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取项目')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='current_pro'))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_current_pro(self,login,data):
        result =BaseInterService.current_pro(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取数据字典')
    @pytest.mark.parametrize('data',yaml_replace_for_filter('base.yml',dir_case='base',filter='data_dict'))
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    def test_base_gain_ITEM_STORE_TYPE(self,login,data):
        result =BaseInterService.data_dict(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1