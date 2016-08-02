# -*- coding: utf-8 -*-
'''
Created on

@author: leng

'''


import requests
import xlrd
import xlwt
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('TestRegister.xls')
# rs = rb.sheet_by_index(0)

wb = copy(rb)

ws = wb.get_sheet(0)
ws.write(4, 4, 'Test')

wb.save('TestRegister.xls')