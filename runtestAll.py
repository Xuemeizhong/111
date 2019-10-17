#encoding: utf-8

import  pytest
import  subprocess

from common.setting import REPORT_HTML,REPORT_XML,CASE_PATH

def invoke(md):
    output, errors = subprocess.Popen(md, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o

if __name__ == "__main__":
    
    #args =['-s','-q' ,'D:\\env-work\\API_TEST\\case\\test_arn_manager.py::TestArnManager::test_arn_manager_query_of_filter','--alluredir',f'{REPORT_XML}']
    #args =['-s','-q' ,'D:\\env-work\\API_TEST\\case\\test_task.py','--alluredir',f'{REPORT_XML}']

   
        # args:
        #     -n 4 分布式执行 多cpu并行执行用例，直接加个-n参数即可，后面num参数就是并行数量，比如num设置为3
        #     -s
        #     -q
    
    #args = ['-n 4','-s', '-q', '--alluredir', f'{REPORT_XML}']
    args =['-s','-q' ,CASE_PATH + '/test_register_of_goods.py::TestRegisterOfGoods::test_arn_receive','--alluredir',f'{REPORT_XML}']
    pytest.main(args)

    cmd = 'allure generate  -c %s -o %s ' % (REPORT_XML, REPORT_HTML)
    invoke(cmd)

