from pmdarima.arima import auto_arima
import matplotlib.pyplot as plt

train, test, x = [],[], []

def modelTraining(data, season, pointer):
	print('Data Received, Training')
	s_model = auto_arima(data, start_p=1, start_q=1, max_p=3, max_q=3,
						 m=season, start_P=0, seasonal=True, d=1, D=1, 
						 trace=True, error_action='ignore', 
						 suppress_warnings=True, stepwise=True)
	print('Training Done')
	print(s_model)
	
	with open('Output'+ str(pointer) +'.txt', 'w') as txt_file:
		txt_file.write(str(s_model))
	
	return s_model
