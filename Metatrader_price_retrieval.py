# typical python stuff, set yourself up for success up here
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
#using Anaconda, matplotlib, metatrader5, and plotly
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import MetaTrader5 as mt5
 
# connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()
 
# request connection status and parameters
print(mt5.terminal_info())
# get data on MetaTrader 5 version
print(mt5.version())
 
# request 1000 ticks from GBPUSD 
gbpusd_ticks = mt5.copy_ticks_from("GBPUSD", datetime(2020,1,28,13), 1000, mt5.COPY_TICKS_ALL)
# request ticks from GBPJPY within 2019.04.01 13:00 - 2019.04.02 13:00
gbpjpy_ticks = mt5.copy_ticks_range("AUDUSD", datetime(2020,1,27,13), datetime(2020,1,28,13), mt5.COPY_TICKS_ALL)
 
# get bars from different symbols in 3 different ways
gbpusd_rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_M1, datetime(2020,1,28,13), 1000)
gbpusd_rates = mt5.copy_rates_from_pos("EURGBP", mt5.TIMEFRAME_M1, 0, 1000)
gbpusd_rates = mt5.copy_rates_range("EURCAD", mt5.TIMEFRAME_M1, datetime(2020,1,27,13), datetime(2020,1,28,13))
 
# shut down connection to MetaTrader 5
mt5.shutdown()
 
#data to be displayed in the terminal
print('gbpusd_ticks(', len(euraud_ticks), ')')
for val in gbpusd_ticks[:1000]: print(val)
 
print('gbpjpy_rates(', len(eurusd_rates), ')')
for val in eurusd_rates[:1000]: print(val)
  
#PLOT
# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(gbpusd_ticks)
ticks_frame = pd.DataFrame(gbpjpy_ticks)
# display ticks on the chart
plt.plot(ticks_frame['time'], ticks_frame['ask'], 'r-', label='ask')
plt.plot(ticks_frame['time'], ticks_frame['bid'], 'b-', label='bid')
 
# display the legends
plt.legend(loc='upper left')
 
# add the header
plt.title('GBPUSD ticks')
 
# display the chart
plt.show()
