import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


'''data =pd.read_csv('Delhi_weather_dataset.csv')
data = data.drop('date',axis=1)
                                                            #cleaning the csv file
data.fillna(0,inplace=True)

data.to_csv('Final_Delhi_weather_dataset.csv',index=False)
#print(data)'''

#taking user input 
t_avg = float(input('Enter the average temperature of New_Delhi in degrees celsius: '))
t_min = float(input('Enter the minimum temperature of New_Delhi in degrees celsius: '))
t_max = float(input('Enter the maximum temperature of New_Delhi in degrees celsius: '))


data = pd.read_csv('Final_Delhi_weather_dataset.csv')

x = data.drop(['pricipitation'],axis=1)#feeding data to the x unit except precipitation
                                       #on which the predicted value(precipitation) is depended
#x = x.values.reshape(-1,1)
#print(x)
y = data['pricipitation'] #taking the value to be predicted(precipitation) to compare with the x unit
y = y.values.reshape(-1,1)
#print(y)

#mainly used for  graphical visualization
day_index = 11798
day = [i for i in range(y.size)]

'''dy = pd.DataFrame(day)
dy.to_csv('Number of days.csv')'''
#print(day)

#training the program for more accurate prediction
li_reg = LinearRegression()
li_reg.fit(x,y)

#taking the sample input to use for prediction
inp = np.array([[t_avg],[t_min],[t_max]])
inp = inp.reshape(1,-1)

#predicting the precipitation
prediction = li_reg.predict(inp)

#used for converting inches to ml units
pred = prediction[0]
predict = pred[0]
ml_precipitation = (0.016387064*predict)*1000


print('Rainfall prediction: ',predict)#main value
print('Rainfall prediction in ml: ',ml_precipitation)

#Plotting graphs
print('The presipitation trend graph:')
plt.scatter(day,y,color='lightgreen')
plt.scatter(day[day_index],y[day_index],color='black')
plt.title('Precipitation Level')

plt.show()