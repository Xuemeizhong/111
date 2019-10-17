#encoding: utf-8


from common.send_all import SendRequest
from common.log import  logger

class HomeService:

    @classmethod
    def home_site(cls,data):
        '''
        获取站点信息
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise

    @classmethod
    def home_warehouse(cls,data):
        '''
        获取仓库信息
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise

    def home_menu(data):
        '''
        获取主页菜单
        :return:
        '''
        try:
            return  SendRequest(data)
        except Exception as error:
            raise