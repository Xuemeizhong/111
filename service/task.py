#encoding: utf-8

from common.send_all import  SendRequest
from common.log import  logger
from common.tools import yaml_replace_for_filter
from service.base import BaseInterService

class taskService:

    @classmethod
    def task_list(cls,data):
        '''

        :param data: 列表查询接口
        :return:
        '''
        try:
            if 'type' in data['data'].keys() and data['data']['type'] != None: 

                type_data = yaml_replace_for_filter('base.yml',dir_case='base',filter='sys_enum')
                type_response = BaseInterService.sys_enum(type_data[0])

                if type_response.status_code == 200:

                    result_type =type_response.json()

                    for index in range(0,len(result_type['data'])):

                        if data['data']['type'] in result_type['data'][index].values():

                            data['data']['type']=result_type['data'][index].get('enumValue')
                            break

            response=  SendRequest(data)
            
            return response
        except Exception as error:
            raise

   

    @classmethod
    def task_list_of_type(cls, type, list):
        '''

        :param type: 任务类型
        :param list: 列表查询接口
        :return:
        '''
        try:

            type_response = BaseInterService.sys_enum(type)
            print(type_response)
            type =type_response.json()['data']
            for index in range(0, len(type)):
                if list['data']['type'] in type[index].values():
                    list['data']['type'] = type[index].get('enumValue')

            response = SendRequest(list)
            
            return response
        except Exception as error:
            raise


if __name__ == "__main__":
    ta = taskService()
    data = yaml_replace_for_filter('task.yml', filter='list',dir_case='task',index=1)
    result =ta.task_list(data)
