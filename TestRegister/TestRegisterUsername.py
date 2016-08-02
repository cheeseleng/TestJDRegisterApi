# -*- coding: utf-8 -*- 
'''
Created on 16/7/26

@author: leng

'''

import requests
import threadpool
import time
from log.log import Log
from Excel.TestCreatExcel import CreatExcel


def Post(Excel_data, Result):
    header = {
        "Host": "reg.jd.com",
        "Origin": "https://reg.jd.com",
        "Referer": "https://reg.jd.com/reg/person?ReturnUrl=http%3A%2F%2Fwww.jd.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.10 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    post_data = {
        "regName": Excel_data['regName'],
        "pin": Excel_data['pin']
    }
    if Excel_data['regName'] == 'NULL':
        del post_data['regName']
    if Excel_data['pin'] == 'NULL':
        del post_data['pin']
    r = requests.session()
    time.sleep(1)
    Result['RunSuccessCount'] += 1
    try:
        Log().loginfo("Starting RTS - " + str(Excel_data['CaseID']))
        r.get('https://reg.jd.com/reg/person?ReturnUrl', headers=header)
        try:
            response = r.post('https://reg.jd.com/validateuser/isPinEngaged', data=post_data, headers=header)
            if '200' in str(response):
                Result['ResponseSuccessCount'] += 1
        except:
            return
        if Excel_data['Result'] in response.content:
            Result['ResultSuccessCount'] += 1
    except Exception as e:
        Log().logerror(e.message)


def multithread():
    Excel_datas = CreatExcel().GetParam()
    Log().__init__()
    threadPoolCount = 5  # 开启的线程数
    func_var = []
    for Excel_data in Excel_datas:
        print Excel_data
        Result = {
            'CaseID': Excel_data['CaseID'],
            'ResponseSuccessCount': 0,
            'RunSuccessCount': 0,
            'ResultSuccessCount': 0
        }
        Log().loginfo("Starting Thread - " + str(Excel_data['CaseID']))
        for i in range(0, 50):  # 每个用例跑50次
            args = ([Excel_data, Result], None)
            func_var.append(args)
        pool = threadpool.ThreadPool(threadPoolCount)
        requestsss = threadpool.makeRequests(Post, func_var)
        [pool.putRequest(req) for req in requestsss]
        pool.wait()
        CreatExcel().SetResult(Result)

multithread()
