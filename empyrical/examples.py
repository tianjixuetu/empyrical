import empyrical 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#读取数据
returns=pd.read_csv('C:/code/empyrical/empyrical/empyrical/tests/test_data/returns.csv',names=['date','rate'])
returns['rate']=returns['rate']/100
rate=returns['rate']
#计算相关的指标
print('计算年化收益率',
        empyrical.annual_return(rate) )
print('计算年化的波动率（标准差)',
        empyrical.annual_volatility(rate))
print('画出累计收益图')
empyrical.cum_returns(rate).plot()
print('计算夏普率',
        empyrical.sharpe_ratio(rate))
print('计算时间序列的稳定程度',
        empyrical.stability_of_timeseries(rate))