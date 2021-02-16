import plotly.express as px 
import csv 
import numpy as np
def plotfigure(datapath):
    with open(datapath)as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x='SizeofTV',y='Averagetimespent')
        fig.show()
def getdatasource(datapath):
    SizeofTV=[]
    Averagetimespent=[]
    with open(datapath)as f:
        df = csv.DictReader(f)
        for row in df:
            SizeofTV.append(float(row['SizeofTV']))
            Averagetimespent.append(float(row['Averagetimespent']))
    return{'x':SizeofTV,'y':Averagetimespent}
def findcorelation(datasource):
    corelation = np.corrcoef(datasource['x'],datasource['y'])
    print(corelation[0,1])
def setup():
    datapath = 'Size of TV,_Average time spent watching TV in a week (hours).csv' 
    datasource = getdatasource(datapath)
    findcorelation(datasource) 
    plotfigure(datapath) 
setup()            
