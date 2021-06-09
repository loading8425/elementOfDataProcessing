import pandas as pd

def get_rate(death, case):
    if death == 0:
        return 0
    else:
        return death/case

def main():
    # read csv file to dataframe
    column_name = ['date', 'location', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']
    data = pd.read_csv('owid-covid-data.csv',parse_dates= ['date'],encoding = 'ISO-8859-1')
    data = data[column_name]

    # delete all other year excpet 2020
    data = data[(data['date'] > '2020-1-1') & (data['date'] <= '2020-12-31')]
    data = data.sort_values(by= 'date')
    data['month'] = data['date'].dt.month

    # create new dataframe for Part A(1)
    data_A1_total_cases = data.groupby(['location','month'],as_index=False).max()
    data_A1_total_cases = data_A1_total_cases[['location', 'month', 'total_cases', 'total_deaths']]
    data_A1_new_cases = data.groupby(['location', 'month'], as_index=False).sum()
    data_A1_new_cases = data_A1_new_cases[['location' ,'month' ,'new_cases', 'new_deaths']]
    data_A1 = pd.merge(data_A1_total_cases, data_A1_new_cases, how='left', on=['location','month'])
    data_A1 = data_A1[['location' ,'month' ,'total_cases','new_cases', 'total_deaths', 'new_deaths']]

    # dataframe for A(2)
    data_A2 = data_A1
    data_A2['case_fatality_rate'] = data_A2.apply(lambda row: get_rate(row['total_deaths'], row['total_cases']), axis = 1)

    #data_A2.index = range(1,len(data_A2) + 1)
    data_A2 = data_A2[['location', 'month', 'case_fatality_rate', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths']]
    print(data_A2.head())
    data_A2.to_csv('owid-covid-data-2020-monthly.csv', index=False)

if __name__ == '__main__':
    main()
