API_TEST
│  README.md
│  requirements.txt
│  runtest.py
│  runtestAll.py
│  start.sh
│
├─API            目前没有使用
│      arn_manager.py
│      login.py
│      __init__.py
│
├─case           测试案例
│      conftest.py
│      test_arn_manager.py
│      test_login.py
│      __init__.py
│
├─common   公共方法
│      find_replace.py
│      log.py
│      logger.py
│      send_all.py
│      setting.py
│      tools.py
│      __init__.py
│
├─data   测试案例数据
│      API.yml
│      arn.yml
│      env.yml
│      login.yml
│
├─log  日志
│      PDA_API_TEST_2019-09-06.log
│      PDA_API_TEST_2019-09-09.log
│
└─report   测试报告






Pytest 库测规则
    文件名以test_*.py文件和*_test.py
    以test_开头的函数
    以Test开头的类
    以test_开头的方法
    所有的包pakege必须要有__init__.py文件


python 命名规范
    模块： 模块尽量使用小写命名，首字母保持小写，尽量不要用下划线(除非多个单词，且数量不多的情况)
    类： 类名使用驼峰(CamelCase)命名风格，首字母大写，私有类可用一个下划线开头
    函数： 函数名一律小写，如有多个单词，用下划线隔开
    变量： 变量名尽量小写, 如有多个单词，用下划线隔开
    常量： 常量使用以下划线分隔的大写命名



allure配置
    1、allure下载地址：https://github.com/allure-framework/allure2/releases
    2、配置allure环境变量

allure常用装饰器
    Features:标注主要功能模块
    Stories:标注Features功能模块下的分支功能
    Title:标注Stories下测试用例名称
    Step:标注测试用例的重要步骤
    Severity:标注测试用例的重要级别
    Description: 标注测试用例的描述

python3 + requests + pytest + allure





