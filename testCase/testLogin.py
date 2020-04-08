import unittest

from common.Log import Logger
from common.MyUnittest import MyUnittest, log
from pageObject.loginPage import LoginPage

log = Logger(__name__)

class TestLogin(MyUnittest):
    def test_01(self):

        """测试"""

        log.logger.info("第一次测试")
        self.login = LoginPage(self.driver)
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
