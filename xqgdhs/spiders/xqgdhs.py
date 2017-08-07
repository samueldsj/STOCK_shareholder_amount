#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:52:20 2017

@author: samuel
"""

import scrapy
import json
#import requests

from xqgdhs.items import XqgdhsItem


class XqgdhsSpider(scrapy.Spider):
    name = 'xqgdhs'
    allowed_domains = ['www.xueqiu.com']    
    start_urls = ('http://www.xueqiu.com')


    def start_requests(self):
        reqs = []
        SHLIST = []
        PRE_SZLIST = []
        #print(self.headers)

        for SH1 in list(range(600000,602000)):# 600000～601999
            SHLIST.append(SH1)
        for SH2 in list(range(603000,604000)):# 603000～603999
            SHLIST.append(SH2)
        for shcounter in range(1,3): #两页可以显示到2004年了
            for sh in SHLIST:
                req = scrapy.Request('https://xueqiu.com/stock/f10/shareholdernum.json?symbol=SH%s&page=%i'%(sh,shcounter))
                reqs.append(req)

        for SZ3 in list(range(300001,300700)):# 300001～300672
            PRE_SZLIST.append(SZ3)
        for SZ1 in list(range(1,1000)): # 000001～000999
            PRE_SZLIST.append(SZ1)
        for SZ2 in list(range(2001,3000)):# 002001～002886
            PRE_SZLIST.append(SZ2)
        for SZLIST in PRE_SZLIST:
            while len(str(SZLIST))<6: #深圳开头，补起前面的0
                SZLIST = '0'+ str(SZLIST)
            for szcounter in range(1,3):

               # print('&&&&&&&&&&&&&&&&7req:',req)
                '''if len(req)>0:   
                    item['NAME'] = SZLIST
                    item['ID'] = SZLIST'''
                
                req = scrapy.Request('https://xueqiu.com/stock/f10/shareholdernum.json?symbol=SZ%s&page=%i'%(SZLIST,szcounter))
                reqs.append(req)
        return reqs


    def parse(self, response):
        datas = json.loads(response.body)              
        item = XqgdhsItem()
        #print('**********url**********',response.url[-13:-7])
        #print('**********datas.get(\'list\')**********',datas.get('list'))
        if datas.get('list'):
            #print(' =        =====  here')
            for data in datas.get('list'):
                #item['NAME'] = data["enddate"]
                item['code'] = response.url[-13:-7]
                item['date'] = data["enddate"]
                item['amount'] = data["totalshamt"]
                yield item