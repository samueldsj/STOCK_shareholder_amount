# STOCK_shareholder_amount
purpose:
fetch and analysis the quantity the shareholder to evaluate the probably percentage gain and duration

content:
data fetch: scrapy files: items.py, pipelines.py, settings.py, xqgdhs.py
data analysis: jupyter notebook: STOCK_shareholder_amount_evaluate.ipynb

目的：
分析个股股东户数变化，并设定一定周期内股东减少比例，分析其后30个日历日的走势。获取后续走势的涨幅概率以及达到峰值的时间周期。

数据获取：
scrapy抓取xueqiu股东户数信息(https://xueqiu.com/stock/f10/shareholdernum.json?symbol=SH%s&page=%i'%(sh,shcounter))
数据分析：jupyter
