import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

test, train, x, tempData = [], [], [], []

def Prediction(data, season, prediction, pointer, dateData):
	h=13

	print('Training Done')
	
	print('Splitting Data For Test')
	
	for i in range(0, len(data)):
		if i<3961:
			train.append(data[i])
		else:
			test.append(data[i])
			x.append(i)
	
	print('Data Splitting Done, Modelling')
	
	if pointer == 0:
		order1 = (2, 1, 1)
		order2 = (2, 1, 2, season)
		
	elif pointer == 1:
		order1 = (1, 1, 2)
		order2 = (1, 1, 1, season)
		
	elif pointer == 2:
		order1 = (2, 1, 1)
		order2 = (0, 1, 1, season)
	
	for d in range(0, 14):
		model = sm.tsa.SARIMAX(train, order=order1,
							   seasonal_order=order2,
							   enforce_invertibility=False, 
							   enforce_stationarity=False)
		

		print('Model Done, Predicting')
		
		tempData = train

		model_fit = model.fit(disp = False)
		output = model_fit.predict(
		start = len(train), end = len(train)+h)
		
		print('Prediction Done, Output = ', output)
		print('Building graph')
			
		plt.plot(x, output, label = 'Forecast')
		plt.plot(x, test, label = 'Known Data')
		
		plt.xlabel('ArrayPosition')

		if pointer == 0:
			plt.ylabel('Temperature')
		elif pointer == 1:
			plt.ylabel('Air-Pressure')
		elif pointer == 2:
			plt.ylabel('Humidity')
		plt.title('TestChart')
		plt.legend()
		plt.show()
		
		tempData.append(test[0])
		del test[0]
		h = h-1
		del x[0]
