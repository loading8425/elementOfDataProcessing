import pandas as pd
import matplotlib.pyplot as plt
import math
import parta1

def get_log(x):
    if x==0:
        return 0
    else:
        return math.log(x)

def main():
    # read csv file to dataframe
    column_name = ['date', 'location', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']
    data = pd.read_csv('owid-covid-data.csv',parse_dates= ['date'],encoding = 'ISO-8859-1')
    data = data[column_name]

    # delete all other year excpet 2020
    data = data[(data['date'] > '2020-1-1') & (data['date'] <= '2020-12-31')]

    #groupby location
    data_sum = data.groupby(['location'], as_index=False).sum()
    data_sum = data_sum[['location','new_cases', 'new_deaths']]
    data_max = data.groupby(['location'], as_index=False).max()
    data_max = data_max[['location','total_cases','total_deaths']]
    data = pd.merge(data_max, data_sum, how='left', on=['location'])
    data['case_fatality_rate'] = data.apply(lambda row: parta1.get_rate(row['total_deaths'], row['total_cases']), axis = 1)

    #plot graph A
    plt.scatter(data.iloc[:,3], data.iloc[:,5], 8,color = 'black')
    plt.ylabel("case_fatality_rate")
    plt.xlabel("new_cases")
    plt.xlim(-100000,800000)
    plt.ylim(0,0.08)
    plt.grid(True)
    plt.savefig('scatter-a.png')

    #plot graph B
    data['new_cases'] = data['new_cases'].apply(get_log)
    plt.scatter(data.iloc[:,3], data.iloc[:,5], 8,color = 'black')
    plt.ylabel("case_fatality_rate")
    plt.xlabel("new_cases(log-scale)")
    plt.xlim(0,30)
    plt.ylim(0,0.08)
    plt.grid(True)
    plt.savefig('scatter-b.png')

if __name__ == '__main__':
    main()