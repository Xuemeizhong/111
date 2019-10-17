#encoding: utf-8


from common.tools import yaml_replace_for_filter
from service.task import taskService
from service.base import BaseInterService
import allure
import  pytest

@allure.feature('任务模块')
class TestTask:


    @allure.title('获取任务列表&&条件查询')
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)
    @pytest.mark.parametrize('data', yaml_replace_for_filter('task.yml',dir_case='task', filter='list'))
    def test_task_list(self,login,data):
        result = taskService.task_list(data)
        assert  result.status_code == 200
        assert result.json()['code'] == 1


    @allure.title('获取任务类型')
    @pytest.mark.parametrize('data', yaml_replace_for_filter('base.yml',dir_case='base', filter='sys_enum',index=1))
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)
    def test_task_type(self, login, data):
        result = BaseInterService.sys_enum(data)
        assert result.status_code == 200
        assert result.json()['code'] == 1


    @allure.title('根据任务类型过滤任务列表')
    @pytest.mark.parametrize('list', yaml_replace_for_filter('task.yml', dir_case='task', filter='list'))
    @pytest.mark.parametrize('type', yaml_replace_for_filter('task.yml', dir_case='task', filter='type'))
    @pytest.mark.parametrize('login', yaml_replace_for_filter('login.yml'), indirect=True)
    def test_task_list_of_type(self, login, type,list):
        result = taskService.task_list_of_type(type,list)
        assert result.status_code == 200
        assert result.json()['code'] == 1


if __name__ == "__main__":
    pytest.main(['-vs','test_task.py'])

