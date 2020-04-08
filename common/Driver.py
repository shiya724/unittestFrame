# coding: utf-8
import sys
from common.Log import Logger
from selenium import webdriver

log = Logger(__name__)

class WbDriver(object):

    def firefox(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            log.logger.exception("FireFoxDriverServer.exe可执行文件必须位于PATH中，请下载并确认！",
                                 exc_info=True)
            raise e
        else:
            log.logger.info(
                '成功找到Firefoxdriver')
            return self.driver

    def chrome(self):
        try:
            option = webdriver.ChromeOptions()
            option.add_argument('--no-sandbox')
            self.driver = webdriver.Chrome(options=option)
        except Exception as e:
            log.logger.exception('ChromeDriverServer.exe可执行文件必须位于PATH中，请下载并确认！',
                             exc_info=True)
            raise e
        else:
            log.logger.info('成功找到chromedriver')
            return self.driver

    def ie(self):
        try:
            self.driver = webdriver.Ie()
        except Exception as e:
            log.logger.exception('IEDriverServer.exe可执行文件必须位于PATH中，请下载并确认！',
                                 exc_info=True)
            raise e
        else:
            log.logger.info('成功找到IEdriver')
            return self.driver


if __name__ == '__main__':
    # wb = WbDriver().chrome()
    # sleep(10)
    # wb.quit()
    pass