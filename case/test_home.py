#encoding: utf-8

import allure
import pytest
from service.home import HomeService
from common.tools import yaml_replace_for_filter

@allure.feature('获取站点')
@allure.tag('site')
class TestHome:

    @allure.title('获取site站点')
    @pytest.mark.parametrize('login',yaml_replace_for_filter('login.yml'),indirect=True)
    @pytest.mark.parametrize('data',yaml_replace_for_filter('home.yml',dir_case='home',filter='site'))
    def test_home_site(self,login,data):
        result =HomeService.home_site(data)
        assert result.status_code == 200
        assert  result.json()['code'] ==1

    @allure.title('获取仓库')
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)
    @pytest.mark.parametrize('data', yaml_replace_for_filter('home.yml',dir_case='home', filter='warehouse'))
    def test_home_warehouse(self, login, data):
        result = HomeService.home_warehouse(data)
        assert result.status_code == 200
        assert result.json()['code'] == 1


    @allure.title('获取主菜单')
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)
    @pytest.mark.parametrize('data', yaml_replace_for_filter('home.yml', dir_case='home',filter='menu'))
    def test_home_menu(self, login, data):
        result = HomeService.home_menu(data)

        assert result.status_code == 200
        assert result.json()['code'] == 1




if __name__ == "__main__":
    pytest.main(["-vs", "test_home_menu"])