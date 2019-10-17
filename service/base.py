#encoding: utf-8
from common.send_all import SendRequest
from common.log import  logger


class BaseInterService:

    @classmethod
    def sys_enum(cls,data):
        '''
        获取系统枚举
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise

    @classmethod
    def current_org(cls,data):
        '''
        获取委托方
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise

            

    @classmethod
    def data_dict(cls,data):
        '''
        获取数据字典
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise

    @classmethod
    def current_pro(cls,data):
        '''
        获取项目
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise

    @classmethod
    def currency_list(cls,data):
        '''
        获取货币类型
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise


    def item_type(cls,data):
        '''
        获取货品类型
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise