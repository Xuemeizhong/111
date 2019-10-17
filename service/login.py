#encoding: utf-8

from common.send_all import SendRequest

from common.tools import yaml_to_json
from common.find_replace import findAndReplace
import  json



class LoginService:

    def login_func(data):
        try:
            return  SendRequest(data)
        except Exception as error:
            raise


#
# def login(func):
#
#     data = json.loads(yaml_to_json('login.yml'))
#     api = json.loads(yaml_to_json('service.yml'))
#     data = findAndReplace(api, json.dumps(data))['login_case_001']
#
#     def warpper(self,*args):
#         try:
#             self.response = login_func(data)
#             return  func(self,*args)
#         except Exception as error:
#             logger.error(f"{self}异常：{error}")
#             raise
#
#     return  warpper
#
# def loginPda(func):
#     data = json.loads(yaml_to_json('login.yml'))
#     api = json.loads(yaml_to_json('service.yml'))
#     data = findAndReplace(api, json.dumps(data))['login_case_001']
#
#     def warpper(*args):
#         try:
#             return  login_func(data)
#         except Exception as error:
#             logger.error(f"异常：{error}")
#             raise
#
#     return warpper


if __name__ =='__main__':

    data =  json.loads(yaml_to_json('login.yml'))
    api= json.loads(yaml_to_json('service.yml'))
    data =findAndReplace(api,json.dumps(data))
    response = login_func(data['login_case_001'])
