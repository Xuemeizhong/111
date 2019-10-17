#encoding: utf-8
import os

import logging
import time
from logging.handlers import TimedRotatingFileHandler
from common.setting import LOG_PATH
from common.tools import get_yaml_date_by_fillter


class TestLogger:

    def __init__(self):

        self.logger = logging.getLogger()
        logging.root.setLevel(logging.NOTSET)
        c = get_yaml_date_by_fillter(filename='env.yml',filter= 'log')
        now = time.strftime('%Y-%m-%d', time.localtime())
        self.log_name = os.path.join(LOG_PATH, 'PDA_API_TEST_{0}.log'.format(time.strftime('%Y-%m-%d')))
        # self.log_name = c.get('file_name') if c and c.get(
        #     'file_name') else  os.path.join(LOG_PATH, 'PDA_API_TEST_{0}.log'.format(time.strftime('%Y-%m-%d')))
        self.backup_count = c.get('backup') if c and c.get('backup') else 5
        self.console_level = c.get('console_level') if c and c.get(
            'console_level') else 'INFO'
        self.file_level = c.get('file_level') if c and c.get(
            'file_level') else 'DEBUG'
        pattern = c.get('pattern') if c and c.get(
            'pattern') else '%(asctime)s - %(filename)s-[%(lineno)s] -%(levelname)s-%(message)s'
        self.formatter = logging.Formatter(pattern)

    @property
    def get_log(self):

        # 避免重复日志
        if not self.logger.handlers:

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(self.formatter)

            console_handler.setLevel(self.console_level)

            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH, self.log_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='UTF-8')

            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_level)
            self.logger.addHandler(file_handler)
        return self.logger





logger = TestLogger().get_log

if __name__ == '__main__':
    logger.info('log config ')
