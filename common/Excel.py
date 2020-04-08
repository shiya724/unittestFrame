import xlrd
import os

from common.Log import Logger
from config import conf

log = Logger(__name__)

class ReadExcel(object):

    def __init__(self,fileName='elementDate.xlsx',sheetName='elementsInfo'):
        try:
            log.logger.info("开始获取[%s]的[%s]表" % (fileName,sheetName))
            self.dataFile = os.path.join(conf.dataPath, fileName)
            self.workBook = xlrd.open_workbook(self.dataFile)
            self.sheetName = self.workBook.sheet_by_name(sheetName) #获取名字为sheetName的工作表
            self.sheet = sheetName
        except Exception:
            log.logger.exception('获取工作表[%s]失败' % sheetName, exc_info=True)
            raise

    def readExcel(self,rownum,colnum):
        try:
            value = self.sheetName.cell(rownum,colnum).value
        except Exception:
            log.logger.exception('读取工作表[%s]数据失败' % self.sheet, exc_info=True)
            raise
        else:
            log.logger.info('成功读取工作表[%s]数据' % self.sheet)
            return value

    #用字典数组形式输出数据
    def readData(self):
        nrows = self.sheetName.nrows
        colNames = self.sheetName.row_values(0)
        list = []
        for rowNum in range(1,nrows):
            row = self.sheetName.row_values(rowNum)
            if row:
                app = {} #定义字典
                for i in range(len(colNames)):
                    if isinstance(row[i],float):
                        row[i] = int(row[i])
                    app[colNames[i]] = row[i]
                list.append(app) #追加
        log.logger.info("创建表[%s]的数据字典" % self.sheet)
        return list

    def getCaseID(self,data):
        list = []
        for i in range(len(data)):
            # print(i)
            id = data[i]["caseId"]
            # print(caseId)
            list.append(id)
        return list

if __name__ == '__main__':
    cellValue = ReadExcel().readExcel(1,3)
    # print((cellValue))
    userData = ReadExcel('elementDate.xlsx', 'userIdPw')
    user = userData.readData()
    # print(user[0]["userId"])
    # print(str(user[6]["password"]))
    # print(user)
    t = userData.getCaseID()
    print(t)