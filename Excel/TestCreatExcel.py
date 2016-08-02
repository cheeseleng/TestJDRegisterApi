# -*- coding: utf-8 -*- 
'''
Created on 16/7/26

@author: leng

'''

import xlrd
from xlutils.copy import copy


class CreatExcel():
    def GetParam(self):
        excel = xlrd.open_workbook('TestRegister.xls')
        Excel_datas = []
        worksheet = excel.sheet_by_index(0)    # 表格Sheet1
        num_rows = worksheet.nrows        # 行数
        for i in range(4, num_rows):
            row = worksheet.row_values(i)
            CaseID = row[0]
            regName = row[1]
            pin = row[2]
            Result = row[3]
            Excel_data = {
                'CaseID': int(CaseID),
                'regName': regName,
                'pin': pin,
                'Result': Result
            }
            Excel_datas.append(Excel_data)
        return Excel_datas

    def SetResult(self, Result):
        excel = xlrd.open_workbook('TestRegister.xls')
        wb = copy(excel)
        ws = wb.get_sheet(0)
        ws.write(Result['CaseID'] + 3, 4, str(Result['RunSuccessCount']) + '/50')
        ws.write(Result['CaseID'] + 3, 5, str(Result['ResponseSuccessCount']) + '/50')
        ws.write(Result['CaseID'] + 3, 6, str(Result['ResultSuccessCount']) + '/50')
        wb.save('TestRegister.xls')


CreatExcel().GetParam()
