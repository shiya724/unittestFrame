# -*- coding: utf-8 -*-
import unittest
from functools import wraps
from time import sleep

from common.Driver import WbDriver
from pageObject.loginPage import LoginPage
from common.Log import Logger

log = Logger(__name__)


def skip_dependon(depend=""):
    """
    :param depend: 依赖的用例函数名，默认为空
    :return: wraper_func
    """
    def wraper_func(test_func):
        @wraps(test_func)  # @wraps：避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("{} cannot depend on itself".format(depend))
            # print("self._outcome", self._outcome.__dict__)
            # 此方法适用于python3.4 +
            # 如果是低版本的python3，请将self._outcome.result修改为self._outcomeForDoCleanups
            # 如果你是python2版本，请将self._outcome.result修改为self._resultForDoCleanups
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            # skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors)
            if failures.find(depend) != -1:
                # 输出结果 [<__main__.TestDemo testMethod=test_login>]
                # 如果依赖的用例名在failures中，则判定为失败，以下两种情况同理
                # find()方法：查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            # elif skipped.find(depend) != -1:
            #     test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)
        return inner_func
    return wraper_func

class MyUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #火狐浏览器
        # cls.driver = WbDriver().firefox()
        cls.driver = WbDriver().chrome()
        log.logger.info('打开浏览器')

    def setUp(self) :
        self.login = LoginPage(self.driver)
        self.login.open()
        log.logger.info('************************ 开始执行测试用例 ************************')

    def tearDown(self) :
        sleep(0.7)
        log.logger.info('************************ 测试用例执行结束 ************************')
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()
        log.logger.info('退出浏览器')

    #登录
    def retryingLogin(self,userId,pwd,userName):
        self.login.loginFunc(userId, pwd)
        if self.driver.current_url != "https://se.dgut.edu.cn/home":
            log.logger.info("重新登录")
            self.login.loginFunc(userId, pwd)
            self.login.isUserNameInWelcomeText(userName)

    def stuLogin(self,userId='201944101202',pwd ='0',userName='陈崇鑫'):
        self.login.loginFunc(userId, pwd)
        if self.driver.current_url != "https://se.dgut.edu.cn/home":
            log.logger.info("重新登录")
            self.login.loginFunc(userId, pwd)
            self.login.isUserNameInWelcomeText(userName)

    def teaLogin(self,userId='2007018',pwd ='0',userName='陈倩'):
        self.login.loginFunc(userId, pwd)
        if self.driver.current_url != "https://se.dgut.edu.cn/home":
            log.logger.info("重新登录")
            self.login.loginFunc(userId, pwd)
            self.login.isUserNameInWelcomeText(userName)

    def adminLogin(self,userId='2013007',pwd ='0',userName='敖欣'):
        self.login.loginFunc(userId, pwd)
        if self.driver.current_url != "https://se.dgut.edu.cn/home":
            log.logger.info("重新登录")
            self.login.loginFunc(userId, pwd)
            self.login.isUserNameInWelcomeText(userName)

if __name__ == '__main__':
    unittest.main()
