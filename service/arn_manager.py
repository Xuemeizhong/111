from common.send_all import SendRequest

from common.tools import yaml_replace_for_filter
from service.base import BaseInterService
from common.log import logger

class ArnManagerService:

    @classmethod
    def arn_query(cls, data):
        '''
        据ARN单号查询ARN信息
        :return:
        '''
        try:
            return SendRequest(data)
        except Exception as error:
            raise

    @classmethod
    def arn_list(cls, data):
        '''
        查询该仓库所有的ARN单
        :return:
        '''
        
        enum_data = yaml_replace_for_filter(test_filename='base.yml',  dir_case='base')

        try:
            # 状态
            if 'status' in data['data'].keys() and data['data']['status'] != None:
                #状态接口测试返回
                result_sta = BaseInterService.sys_enum(enum_data['sys_enum'][1])
                if result_sta.status_code == 200:
                    result_status = result_sta.json()
                    for index in range(0, len(result_status['data'])):
                        if str(data['data']['status']) in result_status['data'][index].values():
                            data['data']['status'] = result_status['data'][index]['enumValue']
                            break

            if 'putawayStatus' in data['data'].keys() and data['data']['putawayStatus'] != None:
                #商家状态列表
                result_putaway =  BaseInterService.sys_enum(enum_data['sys_enum'][2])
                print(f"上架状态：{result_putaway.json()}")
                if result_putaway.status_code == 200:
                    result_putawayStatus= result_putaway.json()
                    for index in range(0, len(result_putawayStatus['data'])):
                        if data['data']['putawayStatus'] in result_putawayStatus['data'][index].values():
                            data['data']['putawayStatus'] = result_putawayStatus['data'][index]['enumValue']
                            break

            if 'businessOrgid' in data['data'].keys() and data['data']['businessOrgid'] != None:
                #委托方
                
                result_current_org = BaseInterService.current_org(enum_data['current_org'][0])
                
                if result_current_org.status_code == 200:
                    result_org= result_current_org.json()
                    for index in range(0, len(result_org['data'])):
                        if data['data']['businessOrgid'] in result_org['data'][index].values():
                            data['data']['businessOrgid'] = result_org['data'][index]['id']
                            break

            if 'projectId' in data['data'].keys() and data['data']['projectId'] != None:
                #项目
                
                result_current_pro = BaseInterService.current_pro(enum_data['current_pro'][0])

                if result_current_pro.status_code == 200:
                    result_pro= result_current_pro.json()
                    
                    for index in range(0, len(result_pro['data'])):
                        if data['data']['projectId'] in result_pro['data'][index].values():
                            data['data']['projectId'] = result_pro['data'][index]['id']
                            break
            
            return SendRequest(data)

        except Exception as error:
            raise

    @classmethod
    def arn_sattus(cls,data):
        '''
        根据ARN单号查询，ARN单可做哪些操作
        :return:
        '''
        try:
            return SendRequest(data)
        except expression as identifier:
            raise