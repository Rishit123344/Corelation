import plotly.express as px 
import csv
import numpy as np 
def plotfigure(datapath):
    with open (datapath)as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x='Temperature',y='Ice-cream')
        fig.show()
def getdatasource(datapath):
    icecreamsales=[]
    temperaturesales=[]
    with open(datapath)as f:
        df = csv.DictReader(f)
        for row in df :
            icecreamsales.append(float(row['Ice-cream']))
            temperaturesales.append(float(row['Temperature']))
    return{'x':icecreamsales,'y':temperaturesales}
def findcorelation(datasource):
    corelation = np.corrcoef(datasource['x'],datasource['y'])
    print(corelation[0,1])   
def setup():
    datapath = 'Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv'
    datasource = getdatasource(datapath)
    findcorelation(datasource)
    plotfigure(datapath)
setup()

              