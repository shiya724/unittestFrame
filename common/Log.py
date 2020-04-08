# coding : GBK
import logging
import os
import time

from config.conf import logPath


class Logger(object):
    def __init__(self, logger):

        '指定保存日志的文件路径，日志级别，以及调用文件,将日志存入到指定的文件中'

        # 创建一个logger(记录器)
        # 日志记录的工作主要由Logger对象来完成。在调用getLogger时要提供Logger的名称
        self.logger = logging.getLogger(logger)
        # 设置日志输出的默认级别
        self.logger.setLevel(logging.DEBUG)

        # 设置日志存放路径，日志文件名
        # 获取本地实际，转换为设置的格式
        rq = time.strftime('%Y-%m-%d %H-%M',time.localtime(time.time()))
        all_log_path = logPath + "\\all_logs\\all_"
        error_log_path = logPath + "\\error_logs\\error_"
        all_log_name = all_log_path + rq + ".log"
        error_log_name = error_log_path + rq + ".log"

        # 创建handler
        # 创建一个handler写入所有日志
        fh = logging.FileHandler(all_log_name)
        fh.setLevel(logging.INFO)
        # 创建一个handler写入错误日志
        eh = logging.FileHandler(error_log_name)
        eh.setLevel(logging.ERROR)
        # 创建一个handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志输出格式
        # 以时间-日志器名称-日志级别-日志内容的形式展示
        all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 以时间-日志器名称-日志级别-文件名-函数行数-错误内容
        error_log_formatter = \
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s -%(lineno)s - %(message)s')

        # 将定义好的输出形式添加到handler
        fh.setFormatter(all_log_formatter)
        ch.setFormatter(all_log_formatter)
        eh.setFormatter(error_log_formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(eh)
        self.logger.addHandler(ch)

    def getLog(self):
        return self.logger


if __name__ == '__main__':

    logger = Logger("hw")

    # 定义的输出级别为debug，所有的级别日志都会输出
    # 级别为Fatal>Error>Warn>Info>Debug
    logger.logger.debug("debug")

    logger.logger.log(logging.ERROR,'%(module)s %(info)s',{'module':'log日志','info':'error'}) #ERROR,log日志 error