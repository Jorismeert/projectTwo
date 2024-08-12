import os, sys, time, random, json, glob, datetime, re
from datetime import datetime
import pandas as pd
import openpyxl

def openWebsite(url = "https://www.google.be"):
    import webbrowser
    try:
        webbrowser.get(using='safari').open(url)
    except webbrowser.Error:
        print("Something went wrong.")


def csvToDataframe(filepath):
    import pandas as pd
    # read the csv 
    df = pd.read_csv(filepath)
    df = pd.DataFrame(df)
    return df

def dfToDictionary(filepath):
    df = csvToDataframe(filepath)
    dict_from_df = df.to_dict(orient='records')
    return dict_from_df
    
def splitString(string):
    # split a string after first capital
    r = re.findall(r'[A-Z][^A-Z]', string)
    print(string)
    result = string.index(r[0])
    print(result)
    return (f'{string[0:result].capitalize()} {string[result:].capitalize()}')

def openPages(filepath):
    import os
    command = f'open -a "Pages" "{filepath}"'
    os.system(command)


def main():
    # openWebsite()
    # print(df)
    # csvToDictionary('citiesBelgium.csv')
    # column_names = [columnName for columnName in df.columns]
    
    bs = csvToDataframe('citiesBelgium.csv')
    bs = bs[['name', 'zipCode', 'province']]
    bsDic = bs.to_dict(orient='records')
    
    newCities = {}
    for record in bsDic:
        newCities[record['name']] = {'zipcode':record['zipCode'],'province': record['province']}

    # print(newCities['Zonhoven']['zipcode'])
        
    # for city, record in newCities.items():
    #     print(city, record['zipcode'], record['province'])
    
    # newdf = pd.DataFrame(newCities) 
    # newdf.to_csv('file1.csv') 
    
    
    # command = f'open -a "Numbers" "{'file1.csv'}"'
    # os.system(command)
    
    # command = f'open "{'file1.csv'}"'
    # os.system(command)







if __name__ == "__main__":
    main()

