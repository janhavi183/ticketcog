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
import os
from matplotlib.figure import Figure
# df_low=data.loc[df['priority_id'] == 1]
data = pd.read_csv("ticketpredictdata3.csv")
df_low=data.loc[data['priority_idup'] == 1]
df_low.to_csv("ticket_low.csv")
data_low = pd.read_csv("ticket_low.csv")
df_med=data.loc[data['priority_idup'] == 2]
df_med.to_csv("ticket_med.csv")
data_med = pd.read_csv("ticket_med.csv")
df_high=data.loc[data['priority_idup'] == 3]
df_high.to_csv("ticket_high.csv")
data_high = pd.read_csv("ticket_high.csv")
li_df = [data_low,data_med,data_high]
print(df_low)
# for j in li_df:
def datalow_priority():
    incfrq = data_low.loc[:,['created_at','priority_idup']]
    incfrq.head()
    for i in range(len(incfrq.created_at)):
            if (incfrq.created_at[i][1]=='/'):
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d/%m/%Y %H:%M').date()
            elif (incfrq.created_at[i][2]=='/'):
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d/%m/%Y %H:%M').date()
            else:
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d-%m-%Y %H:%M').date()        

    incfrq['No_Incidents'] = incfrq.groupby('created_at')['priority_idup'].transform('count')
    incfrq.drop(['priority_idup'],axis=1,inplace=True)
    incfrq.drop_duplicates(inplace=True)
    incfrq = incfrq.set_index('created_at')
    incfrq.index = pd.to_datetime(incfrq.index)
    incfrq.head()

    data1 = incfrq['No_Incidents']
    data1 = data1.asfreq('D')
    data1.index

    figure1 = data1.plot(figsize=(15,6))
    fig = figure1.figure
    # figure2 = data2.plot(figsize=(15,6))
    # fig2 = figure2.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datalow_1"

    
    fig.savefig(results_dir + sample_file_name)
    plt.close()
    # fig2.savefig('z2.png')
    plt.show()
    # if j==li_df[0]:
    #     fig.savefig('1_low.png')
    # elif j==li_df[1]:
    #     fig.savefig('1_med.png')
    # else:
    #     fig.savefig('1_high.png')


    incfrom2013 = incfrq[incfrq.index > dt.datetime(2022,10,1)]
    data2 = incfrom2013['No_Incidents']
    data2 = data2.asfreq('D')
    data2.index
    # data2,fill(na)
    figure2 = data2.plot(figsize=(15,6))
    fig2 = figure2.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datalow_2"

    
    fig2.savefig(results_dir + sample_file_name)
    plt.close()
    # fig2.savefig('z2.png')
    plt.show()


    # figure2 = data2.plot(figsize=(15,6))
    # fig2 = figure2.figure
    # if j ==li_df[0]:
    #     fig2.savefig('2_low.png')
    # elif j==li_df[1]:
    #     fig2.savefig('2_med.png')
    # else:
    #     fig2.savefig('2_high.png')
    # # fig2.savefig('2_low.png')
    # plt.show()

    p = d = q = range(0,2)
    pdq = list(itertools.product(p,d,q))

    for param in pdq:
        mod = sm.tsa.statespace.SARIMAX(data2,order=param,enforce_stationarity=False,enforce_invertibility=False)
        results = mod.fit()

    mod = sm.tsa.statespace.SARIMAX(data2,order=(1,1,1))
    results = mod.fit()

    pred = results.get_prediction(start=pd.to_datetime('2022-12-12'),end=pd.to_datetime('2022-12-30'),dynamic=False)
    pred_ci = pred.conf_int()
    pred.predicted_mean.round()

    ax = data2['2022':].plot(label='observed')
    ax.fill_between(pred_ci.index,pred_ci.iloc[:,0],pred_ci.iloc[:,1],color='grey',alpha=0.3)
    ax.set_xlabel('Date')
    plt.legend()
    figure11 = pred.predicted_mean.plot(ax=ax,label='One-step ahead Forecast',figsize=(10, 6))
    fig11 = figure11.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datalow_3"

    
    fig11.savefig(results_dir + sample_file_name)
    plt.close()
    return
def datamed_priority():
    incfrq = data_med.loc[:,['created_at','priority_idup']]
    incfrq.head()
    for i in range(len(incfrq.created_at)):
            if (incfrq.created_at[i][1]=='/'):
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d/%m/%Y %H:%M').date()
            elif (incfrq.created_at[i][2]=='/'):
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d/%m/%Y %H:%M').date()
            else:
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d-%m-%Y %H:%M').date()        

    incfrq['No_Incidents'] = incfrq.groupby('created_at')['priority_idup'].transform('count')
    incfrq.drop(['priority_idup'],axis=1,inplace=True)
    incfrq.drop_duplicates(inplace=True)
    incfrq = incfrq.set_index('created_at')
    incfrq.index = pd.to_datetime(incfrq.index)
    incfrq.head()

    data1 = incfrq['No_Incidents']
    data1 = data1.asfreq('D')
    data1.index

    figure1 = data1.plot(figsize=(15,6))
    fig = figure1.figure
    # figure2 = data2.plot(figsize=(15,6))
    # fig2 = figure2.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datamed_1"

    
    fig.savefig(results_dir + sample_file_name)
    plt.close()
    # fig2.savefig('z2.png')
    plt.show()
    # if j==li_df[0]:
    #     fig.savefig('1_low.png')
    # elif j==li_df[1]:
    #     fig.savefig('1_med.png')
    # else:
    #     fig.savefig('1_high.png')


    incfrom2013 = incfrq[incfrq.index > dt.datetime(2022,10,1)]
    data2 = incfrom2013['No_Incidents']
    data2 = data2.asfreq('D')
    data2.index
    figure2 = data2.plot(figsize=(15,6))
    fig2 = figure2.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datamed_2"

    
    fig2.savefig(results_dir + sample_file_name)
    plt.close()
    # fig2.savefig('z2.png')
    plt.show()


    # figure2 = data2.plot(figsize=(15,6))
    # fig2 = figure2.figure
    # if j ==li_df[0]:
    #     fig2.savefig('2_low.png')
    # elif j==li_df[1]:
    #     fig2.savefig('2_med.png')
    # else:
    #     fig2.savefig('2_high.png')
    # # fig2.savefig('2_low.png')
    # plt.show()

    p = d = q = range(0,2)
    pdq = list(itertools.product(p,d,q))

    for param in pdq:
        mod = sm.tsa.statespace.SARIMAX(data2,order=param,enforce_stationarity=False,enforce_invertibility=False)
        results = mod.fit()

    mod = sm.tsa.statespace.SARIMAX(data2,order=(1,1,1))
    results = mod.fit()

    pred = results.get_prediction(start=pd.to_datetime('2022-12-12'),end=pd.to_datetime('2022-12-30'),dynamic=False)
    pred_ci = pred.conf_int()
    pred.predicted_mean.round()

    ax = data2['2022':].plot(label='observed')
    ax.fill_between(pred_ci.index,pred_ci.iloc[:,0],pred_ci.iloc[:,1],color='grey',alpha=0.3)
    ax.set_xlabel('Date')
    plt.legend()
    figure11 = pred.predicted_mean.plot(ax=ax,label='One-step ahead Forecast',figsize=(10, 6))
    fig11 = figure11.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datamed_3"

    
    fig11.savefig(results_dir + sample_file_name)
    plt.close()
    return
def datahigh_priority():
    incfrq = data_high.loc[:,['created_at','priority_idup']]
    incfrq.head()
    for i in range(len(incfrq.created_at)):
            if (incfrq.created_at[i][1]=='/'):
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d/%m/%Y %H:%M').date()
            elif (incfrq.created_at[i][2]=='/'):
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d/%m/%Y %H:%M').date()
            else:
                incfrq.created_at[i] = dt.datetime.strptime(incfrq.created_at[i],'%d-%m-%Y %H:%M').date()        

    incfrq['No_Incidents'] = incfrq.groupby('created_at')['priority_idup'].transform('count')
    incfrq.drop(['priority_idup'],axis=1,inplace=True)
    incfrq.drop_duplicates(inplace=True)
    incfrq = incfrq.set_index('created_at')
    incfrq.index = pd.to_datetime(incfrq.index)
    incfrq.head()

    data1 = incfrq['No_Incidents']
    data1 = data1.asfreq('D')
    data1.index

    figure1 = data1.plot(figsize=(15,6))
    fig = figure1.figure
    # figure2 = data2.plot(figsize=(15,6))
    # fig2 = figure2.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datahigh_1"

    
    fig.savefig(results_dir + sample_file_name)
    plt.close()
    # fig2.savefig('z2.png')
    plt.show()
    # if j==li_df[0]:
    #     fig.savefig('1_low.png')
    # elif j==li_df[1]:
    #     fig.savefig('1_med.png')
    # else:
    #     fig.savefig('1_high.png')


    incfrom2013 = incfrq[incfrq.index > dt.datetime(2022,10,1)]
    data2 = incfrom2013['No_Incidents']
    data2 = data2.asfreq('D')
    data2.index
    figure2 = data2.plot(figsize=(15,6))
    fig2 = figure2.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datahigh_2"

    
    fig2.savefig(results_dir + sample_file_name)
    plt.close()
    # fig2.savefig('z2.png')
    plt.show()


    # figure2 = data2.plot(figsize=(15,6))
    # fig2 = figure2.figure
    # if j ==li_df[0]:
    #     fig2.savefig('2_low.png')
    # elif j==li_df[1]:
    #     fig2.savefig('2_med.png')
    # else:
    #     fig2.savefig('2_high.png')
    # # fig2.savefig('2_low.png')
    # plt.show()

    p = d = q = range(0,2)
    pdq = list(itertools.product(p,d,q))

    for param in pdq:
        mod = sm.tsa.statespace.SARIMAX(data2,order=param,enforce_stationarity=False,enforce_invertibility=False)
        results = mod.fit()

    mod = sm.tsa.statespace.SARIMAX(data2,order=(1,1,1))
    results = mod.fit()

    pred = results.get_prediction(start=pd.to_datetime('2022-12-12'),end=pd.to_datetime('2022-12-30'),dynamic=False)
    pred_ci = pred.conf_int()
    pred.predicted_mean.round()

    ax = data2['2022':].plot(label='observed')
    ax.fill_between(pred_ci.index,pred_ci.iloc[:,0],pred_ci.iloc[:,1],color='grey',alpha=0.3)
    ax.set_xlabel('Date')
    plt.legend()
    figure11 = pred.predicted_mean.plot(ax=ax,label='One-step ahead Forecast',figsize=(10, 6))
    fig11 = figure11.figure
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, 'static/')
    sample_file_name = "datahigh_3"

    
    fig11.savefig(results_dir + sample_file_name)
    plt.close()
    return
# datahigh_priority()
# datalow_priority()
# datamed_priority()

    # if j ==li_df[0]:
    #     fig.savefig('3_low.png')
    # elif j ==li_df[1]:
    #     fig.savefig('3_med.png')
    # else:
    #     fig.savefig('3_high.png')
    # # fig11.savefig('3_low.png')
    # plt.show()
