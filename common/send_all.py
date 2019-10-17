import  requests,json

from common.log import logger

API = requests.session()
def SendRequest(data):
    if isinstance(data,dict):
        method = data['method']
        headers = data['headers']
        host = data['host']
        api = data['url']
        param = data['data']
        url =f"{host}{api}"
        logger.info(f"请求方式：{method}")
        logger.info(f"请求头：{headers}")
        logger.info(f"请求数据：{data}")
        
        try:
            if method.lower() == 'post' and 'parameters' not in data.keys():
                return  API.post(url=url, json=param, headers=headers)

            if 'parameters' in data.keys():
                argument = data['parameters']
                return   API.post(url=url,params=argument, json=param, headers=headers)

            elif method.lower() == 'get':
                return  API.get(url=url, params=param,  headers=headers)

            elif method.lower() == 'put':
                return API.put(url=url, params=param,  headers=headers)



        except Exception as error:
            logger.error(f"异常信息： {error}")
    else:
        logger.info(f'数据类型不正确：{type(data)}\n{data}')



def sendAll(method,url,data,**kwargs):
    cookie = kwargs.get('cookie')
    headers= kwargs.get('headers')

    try:
        if method.lower() == 'post':
            return requests.post(url=url,json=data,cookies=cookie,headers=headers)
        elif method.lower() =='get':
            return requests.get(url=url,params=data,cookies=cookie,headers=headers)
        elif method.lower() == 'put':
            return requests.put(url=url, params=data, cookies=cookie, headers=headers)
    except Exception as error:
        logger.error(f"异常信息： {error}")
        logger.info(f'请求方式{method}错误')



