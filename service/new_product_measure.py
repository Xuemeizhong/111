from common.send_all import SendRequest
from common.logger import logger
class NewProductMeasureService:
    '''
    ARN单作业状态
    '''
    @classmethod
    def get_five_items(self,data):
        '''
        :param data:
        :return:
        获取料五项
        '''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise 
    @classmethod
    def get_goods_info(cls,data):
        '''新品测量-获取货品信息'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise
    @classmethod
    def get_unit_level(cls,data):
        '''新品测量-获取单位级别 '''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise
    @classmethod
    def get_part_type(cls,data):
        '''新品测量-获取件型 '''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise

    @classmethod
    def get_unit_name(cls, data):
        '''新品测量-获取单位名称'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise

    @classmethod
    def get_goods_type(cls, data):
        '''新品测量-获取货品分类'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise

    @classmethod
    def get_storage_type(cls, data):
        '''新品测量-获取存储分类'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise

    @classmethod
    def get_logistics_type(cls, data):
        '''新品测量-获取物流类型'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise

    @classmethod
    def get_currency(cls, data):
        '''新品测量-获取币种'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise

    @classmethod
    def get_lot_tracking(cls, data):
        '''新品测量-获取批次跟踪属性'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise

    @classmethod
    def save_package_unit(cls, data):
        '''新品测量-保存包装单位'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise

    @classmethod
    def measure_new_item(cls, data):
        '''新品测量-提交'''
        try:
            request = SendRequest(data=data)
            logger.info(f"接口响应返回结果：{request.json()}")
            return request
        except Exception as e:
            raise