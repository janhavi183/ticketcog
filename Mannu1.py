import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import itertools
import statsmodels.api as sm
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
Fulldata = pd.read_csv("ticketpredictdata3febedit.csv")



def ticket_plot(data, priority):

    # Imporing the necessary columns
    incfrq = data.loc[:,['ticketid','created_at']]
    # for i in range(len(incfrq.created_at)):
    #     incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d-%m-%Y %H:%M').date()
    # print(incfrq.head())
    # Coverting all the values in proper Datetime format
    # print(incfrq.head())
    # Adding a new column which will have the number of tickets per day
    incfrq['No_Incidents'] = incfrq.groupby('created_at')['ticketid'].transform('count')
    incfrq.drop(['ticketid'],axis=1,inplace=True)
    incfrq.drop_duplicates(inplace=True)
    # print(incfrq.head(3))
    # Setting Date as the Index
    incfrq = incfrq.set_index('created_at')
    incfrq.index = pd.to_datetime(incfrq.index)
    # print(incfrq.index)
    # print(incfrq.head())
    # Making a new Series with frequency as Day
    data1 = incfrq['No_Incidents']
    data1 = data1.asfreq('D')
    data1  = data1 .fillna(0)
    data1.index
    # print(data1.index)
    # print(data1.head())
    # Plotting number of tickets per day
    figure1 = data1.plot(figsize=(10,6))
    fig = figure1.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    # sample_file_name = "plot1"

    
    # fig.savefig(results_dir + sample_file_name)
    fig.savefig(results_dir +'shp1'+str(priority)+'.png')

    # Since not many tickets before October 2013, we consider only the latter values
    incfrom2013 = incfrq[incfrq.index > dt.datetime(2022,10,1)]
    # print(incfrom2013.head())
    # new Series
    data2 = incfrom2013['No_Incidents']
    data2 = data2.asfreq('D')
    data2 = data2.fillna(0)
    data2.index
    # Plotting number of tickets per day after October 2013

    figure2 = data2.plot(figsize=(10,6))
    fig2 = figure2.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    # sample_file_name = "plot1"

    
    # fig.savefig(results_dir + sample_file_name)
    fig2.savefig(results_dir +'shp2'+str(priority)+'.png')
    # fig2.savefig('shp2'+str(priority)+'.png')
    # plt.show()
    plt.close()
    # Making a list of values for p,d & q
    p = d = q = range(0,2)
    pdq = list(itertools.product(p,d,q))
    # Checking the AIC values per pairs
    for param in pdq:
        mod = sm.tsa.statespace.SARIMAX(data2,order=param,enforce_stationarity=False,enforce_invertibility=False)
        results = mod.fit()
        # print('ARIMA{} - AIC:{}'.format(param, results.aic))
    # Choosing the model with minimum AIC and the ARIMA Model for Time Series Forecasting
    mod = sm.tsa.statespace.SARIMAX(data2,order=(3,1,4))
    results = mod.fit()
    # print(results.summary().tables[1])
    # Predicting the future values and the confidence interval
    pred = results.get_prediction(start=pd.to_datetime('2023-02-02'),end=pd.to_datetime('2023-02-10'),dynamic=False)
    pred_ci = pred.conf_int()
    pred.predicted_mean.round()
    ax = data2['2022':].plot(label='observed')
    ax.fill_between(pred_ci.index,pred_ci.iloc[:,0],pred_ci.iloc[:,1],color='grey',alpha=0.2)
    ax.set_xlabel('Date')
    plt.legend()
    figure11 = pred.predicted_mean.plot(ax=ax,label='One-step ahead Forecast',figsize=(10, 6))
    fig11 = figure11.figure
    # fig11.savefig('shp3'+str(priority)+'.png')
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = 'shp3'+str(priority)+'.png'

    
    fig11.savefig(results_dir + sample_file_name)
    # plt.show()
    plt.close()
    return
def priorityfunction():
    priorityList = Fulldata.priority_idup.unique()
    priorityList = [1,2,3,4]
    for p in priorityList:
        print(p)
        FilteredData = Fulldata[Fulldata['priority_idup'] == p] 
        ticket_plot(FilteredData,p)
priorityfunction()

    # return render_template('untitled1.html', name = 'new_plot', url ='z1.png')
    # return fig
# ticketplot()