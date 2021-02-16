import plotly.express as px 
import csv
import numpy as np 
def plotfigure(datapath):
    with open (datapath)as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x='Marks',y='Days')
        fig.show()
def getdatasource(datapath):
    Markssales=[]
    dayssales=[]
    with open(datapath)as f:
        df = csv.DictReader(f)
        for row in df :
            dayssales.append(float(row['Days']))
            Markssales.append(float(row['Marks']))
    return{'x':Markssales,'y':dayssales}
def findcorelation(datasource):
    corelation = np.corrcoef(datasource['x'],datasource['y'])
    print(corelation[0,1])   
def setup():
    datapath = 'Student Marks vs Days Present.csv'
    datasource = getdatasource(datapath)
    findcorelation(datasource)
    plotfigure(datapath)
setup()

              