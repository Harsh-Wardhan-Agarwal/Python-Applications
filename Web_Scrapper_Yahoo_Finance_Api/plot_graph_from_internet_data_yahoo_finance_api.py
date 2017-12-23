import matplotlib.pyplot as plt
import numpy as np
import urllib
import matplotlib.dates as mdates

def bytespdate2num(fmt, encoding='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s = b.decode(encoding)
		return strconverter(s)
	return bytesconverter

def graph_data(stock):


	fig = plt.figure()																			# Graph customiztaion
	ax1 = plt.subplot2grid((1,1),(0,0))															# Graph customiztaion


	stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
	source_code = urllib.request.urlopen(stock_price_url).read().decode()
	# values:Date,close,high,low,open,volume
	stock_data = []
	source_code_split = source_code.split('\n')
	for line in source_code_split:
		split_line = line.split(',')
		if len(split_line) == 6:
			if 'values' not in line:
				stock_data.append(line)
# %Y -> 2015
# %y -> 15
# %m -> numbermonth
# %d -> number day
# %H -> Hours
# %M -> Minutes
# %S -> Seconds
# 12-06-2014 -> %m-%d-%Y
	date,closep,highp,lowp,openp,volume = np.loadtxt(stock_data,
												  	delimiter=',',
												  	unpack=True,
												  	converters={0:bytespdate2num('%Y%m%d')})



	ax1.plot_date(date,closep,'-', label='Price')		
	ax1.fill_between(date, closep, closep[0], where=(closep>closep[0]), facecolor='g', alpha = 0.5)
	ax1.fill_between(date, closep, closep[0], where=(closep<closep[0]), facecolor='R', alpha = 0.5)										# Graph customiztaion
	for label in ax1.xaxis.get_ticklabels():													# Graph customiztaion
		label.set_rotation(45)																	# Graph customiztaion

	ax1.grid(True, color='g', linestyle='-', linewidth=1)										# Graph customiztaion
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.legend()
	plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.9, wspace=0.2, hspace=0)       # Graph customiztaion
	plt.show()

graph_data('TWTR')
