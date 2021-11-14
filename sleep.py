import csv
import numpy as n
from numpy.lib.function_base import corrcoef
import plotly.express as p

def Plot(data_path):
    with open(data_path) as csv_file:
        
        df = csv.DictReader(csv_file)
        fig = p.scatter(df,x='Coffee(ml)', y=' Sleep(hrs)')
        fig.show()

def getData(data_path):
    coffee = []
    sleep = []

    with open(data_path) as csv_file:
        
        df = csv.DictReader(csv_file)
        for row in df:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    
    return{"x":coffee, "y":sleep}

def findCorrelation(dataSource):
    cor = n.corrcoef(x=dataSource['x'],y=dataSource['y'])
    print("Correlation is :- \n--->",cor[0,1])

def setup():
    data_path = 'Deprivation.csv'
    dataSource = getData(data_path)
    findCorrelation(dataSource)

setup()