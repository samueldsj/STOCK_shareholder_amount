# STOCK_shareholder_amount
[Purpose]:
fetch and analysis the quantity the shareholder to evaluate the probably percentage gain and duration

[data acquisition]:
From: https://xueqiu.com/stock/f10/shareholdernum.json?symbol=SH%s&page=%i'%(sh,shcounter)
By: Scrapy
Content: xqdghs

[data storage]:
Mysql: Xq_gdhs

[data analysis]:
By: Jupyter notebook
Content: STOCK_shareholder_amount_evaluate.ipynb


目的：
分析个股股东户数变化，并设定一定周期内股东减少比例，分析其后30个日历日的走势。获取后续走势的涨幅概率以及达到峰值的时间周期。

数据获取：
scrapy抓取 雪球 股东户数信息(https://xueqiu.com/stock/f10/shareholdernum.json?symbol=SH%s&page=%i'%(sh,shcounter)
文件名：xqdghs

数据存储:
Mysql: Xq_gdhs

数据分析：jupyter
文件名：STOCK_shareholder_amount_evaluate.ipynb
