#encoding: utf-8

import yaml

import json
import os
from common.setting import  DATA_PATH
from ruamel.yaml.util import load_yaml_guess_indent
from ruamel.yaml import  round_trip_dump
from common.find_replace import findAndReplace

def yaml_to_json(filename,dir_path =DATA_PATH):
    '''
        获取yaml文件数据
    :param filename: 文件名称
    :param dir_path: 文件路径
    :return:
    '''
    data_url = os.path.join(dir_path, filename)
    if os.path.exists(data_url):
        with open(data_url, 'r', encoding='UTF-8') as f:
            # ensure_ascii 不适用ascii码 防止中文编译为ascii码
            return json.dumps(yaml.load(f,Loader=yaml.Loader), ensure_ascii=False)
    else:
        raise FileNotFoundError('文件 %s 不存在' % data_url)


def json_to_yaml(filename,json_data,dir_path=DATA_PATH):
    '''
        将数据写入到文件中
    :param filename: 文件名称
    :param json_data:  写入数据
    :param dir_path: 文件路径
    :return:
    '''
    data_url = os.path.join(dir_path, filename)
    if os.path.exists(data_url):
        with open(data_url, 'a+') as f:
            # default_style 不为空即为格式化输出
            yaml.dump(json.loads(json_data), f, indent=4, default_style='a')
    else:
        raise FileNotFoundError('文件不存在')


def get_yaml_date_by_fillter(filename,filter,dir_path=DATA_PATH,  index=0):
    '''
        根据耳机关键字获取测试案例
    :param filename:  测试案例文件名称
    :param filter: 测试案例关键字
    :param dir_path: 文件路径
    :param index: 没用
    :return:  测试案例测试数据
    '''

    #__data = json.loads(yaml_to_json(filename,dir_path),object_pairs_hook=OrderedDict)

    #使用ddt.data方法在yaml中不用添加 -
    __data = json.loads(yaml_to_json(filename, dir_path))
    if  filter ==None:
        return  __data
    else:
        return __data[filter]




def get_yaml_json(filename,dir_path=DATA_PATH,filter=None):
    '''
    获取yaml文件数据
    :param filename: 文件名称
    :param dir_path: 文件路径
    :param filter: 一级关键字
    :return:
    '''
    file_url =os.path.join(dir_path,filename)
    try:
        with open(file_url,encoding='UTF-8') as fp:

            data,ind,bsi =  load_yaml_guess_indent(fp)

            if filter in data and filter !=None:
                return data[filter]
            return  data
    except Exception as error:
        raise  error


def update_yaml_from_filter(filename,data,dir_path=DATA_PATH,ind=None,bsi=None):
    '''
    更新yaml文件
    :param filename: 文件名称
    :param data: 写入数据
    :param dir_path: 文件路径
    :param ind:
    :param bsi:
    :return:
    '''
    file_url =os.path.join(dir_path,filename)
    try:
         with open(file_url,'w',encoding='utf-8') as fp:
            round_trip_dump(data=data,stream=fp,block_seq_indent=bsi,indent=ind)
    except Exception as error:
        print('异常')
        raise  error



def yaml_replace_for_filter(test_filename,dir_case=None,env_filename='API.yml',filter=None,index=None):
    '''

    :param test_filename:  测试案例名称
    :param case_path: data目录下目录名称
    :param env_filename:  公共参数文件
    :param filter: 关键值
    :param index: 索引下表(从1 开始)
    :return:
    '''
    #case_path = os.path.join(DATA_PATH,dir_case)
    case_path = DATA_PATH+ str(dir_case)
    if dir_case!=None:
        case_path = os.path.join(DATA_PATH,dir_case)
    else:
        case_path=DATA_PATH
    data = json.loads(yaml_to_json(filename=test_filename,dir_path=case_path))
    if env_filename!= 'API.yml':
        api = json.loads(yaml_to_json(env_filename))
    else:
        api = json.loads(yaml_to_json('API.yml'))

    if filter != None and index == None:
        return findAndReplace(api,json.dumps(data))[filter]
    elif filter !=None and index !=None:
        result =findAndReplace(api, json.dumps(data))[filter]
        #当索引大于列表长度 默认为最后一个元素
        if index>=len(result):
            return findAndReplace(api, json.dumps(data))[filter][len(result)-1:len(result)]
        else:
            return findAndReplace(api, json.dumps(data))[filter][index-1:index]
    else:
        return  findAndReplace(api, json.dumps(data))




if __name__ == "__main__":
    data=yaml_replace_for_filter('base.yml',filter='sys_enum',dir_case='base',index=3)
    print(type(data))
    print(data)
    print(f"-----------------------------------")
    

