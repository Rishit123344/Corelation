import plotly.express as px 
import csv
import numpy as np 
def plotfigure(datapath):
    with open (datapath)as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x='Coffee',y='sleep')
        fig.show()
def getdatasource(datapath):
    coffeesales=[]
    hoursofsleep=[]
    with open(datapath)as f:
        df = csv.DictReader(f)
        for row in df :
            hoursofsleep.append(float(row['sleep']))
            coffeesales.append(float(row['Coffee']))
    return{'x':coffeesales,'y':hoursofsleep}
def findcorelation(datasource):
    corelation = np.corrcoef(datasource['x'],datasource['y'])
    print(corelation[0,1])   
def setup():
    datapath = 'cups of coffee vs hours of sleep.csv'
    datasource = getdatasource(datapath)
    findcorelation(datasource)
    plotfigure(datapath)
setup()

              