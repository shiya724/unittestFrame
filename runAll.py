import os
import time
import unittest

from common.HTMLTestRunner import HTMLTestRunner
from common.Log import Logger
from config.conf import casePath, reportPath

log = Logger(__name__)


if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    reportName = "测试报告" + now + ".html"
    desc = "报告描述"
    path = os.path.join(reportPath, reportName)

    discover = unittest.defaultTestLoader.discover(casePath, pattern="testLogin.py", top_level_dir=None)
    suite = unittest.TestSuite()
    suite.addTest(discover)
    with open(path, "wb") as report:
        runner = HTMLTestRunner(stream=report, title="测试报告标题", description=desc)
        runner.run(suite)

    report.close()
