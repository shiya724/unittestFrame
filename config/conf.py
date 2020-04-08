import os
import configparser

# 获取当前路径
currPath = os.path.split(os.path.realpath(__file__))[0]
# print(currPath)

# 读配置文件获取项目路径
conf = configparser.ConfigParser()
ini = os.path.join(currPath, "config.ini")
conf.read(ini)
proPath = conf.get("project", "project_path")
# print(proPath)

# 电脑分辨率
computerWidth = conf.get("computer", "width")
computerHeight = conf.get("computer", "height")


# 获取测试数据路径
dataPath = os.path.join(proPath, "textData")
# print(dataPath)

# 获取日志路径
logPath = os.path.join(proPath, 'log')

# 保存截图路径
# 错误截图
failImagePath = os.path.join(proPath, 'report', 'image', 'fail')
# 成功截图
passImagePath = os.path.join(proPath, 'report', 'image', 'pass')

# 获取测试报告路径
reportPath = os.path.join(proPath, 'report')
# 获取测试用例路径
casePath = os.path.join(proPath, 'testCase')

