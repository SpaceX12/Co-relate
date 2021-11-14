import csv
import numpy as n
from numpy.lib.function_base import corrcoef
import plotly.express as p

def Plot(data_path):
    with open(data_path) as csv_file:
        
        df = csv.DictReader(csv_file)
        fig = p.scatter(df,x='Precentage', y=' Days Present')
        fig.show()

def getData(data_path):
    percent = []
    dayPresent = []

    with open(data_path) as csv_file:
        
        df = csv.DictReader(csv_file)
        for row in df:
            percent.append(float(row['Marks In Percentage']))
            dayPresent.append(float(row['Days Present']))
    
    return{"x":percent, "y":dayPresent}

def findCorrelation(dataSource):
    cor = n.corrcoef(x=dataSource['x'],y=dataSource['y'])
    print("Correlation is :- \n--->",cor[0,1])

def setup():
    data_path = 'Attendance.csv'
    dataSource = getData(data_path)
    findCorrelation(dataSource)

setup()
