#encoding: utf-8
from common.send_all import SendRequest

'''
按货品登记
'''
class RegisterOfGoodsService:

    @classmethod
    def arn_search_list(cls,data):
        '''
        获取ARN单中可收获登记列表
        :return:
        '''
        try:
            return SendRequest(data)
        except Exception as error:
            raise


    def resgister():
        pass