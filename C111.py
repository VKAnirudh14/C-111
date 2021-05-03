import plotly.figure_factory as ff 
import pandas as pd 
import csv 
import statistics
import random
import plotly.graph_objects as go 

df=pd.read_csv("data1.csv")
data=df["Math_score"].tolist()


def RandomSetOfValues(counter):
    dataset=[]
    
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data))
        value=data[randomIndex]
        dataset.append(value)
        mean=statistics.mean(dataset)
        return mean

MeanList=[]
for i in range(0,100):
    SetOfMeans=RandomSetOfValues(100)
    MeanList.append(SetOfMeans)

mean=statistics.mean(MeanList)
stdev=statistics.stdev(MeanList)
print("Mean Is ",mean)
print("Standard Deviation Is ",stdev)
firstStdevStart,firstStdevEnd=mean-stdev,mean+stdev
secondStdevStart,secondStdevEnd=mean-(2*stdev),mean+(2*stdev)
thirdStdevStart,thirdStdevEnd=mean-(3*stdev),mean+(3*stdev)
print("stdev1",firstStdevStart,firstStdevEnd)
print("stdev2",secondStdevStart,secondStdevEnd)
print("stdev3",thirdStdevStart,thirdStdevEnd)
fig=ff.create_distplot([MeanList],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[firstStdevStart,firstStdevStart],y=[0,0.17],mode="lines",name="Standard Deviation One Start"))
fig.add_trace(go.Scatter(x=[firstStdevEnd,firstStdevEnd],y=[0,0.17],mode="lines",name="Standard Deviation One End"))
fig.add_trace(go.Scatter(x=[secondStdevStart,secondStdevStart],y=[0,0.17],mode="lines",name="Standard Deviation Two Start"))
fig.add_trace(go.Scatter(x=[secondStdevEnd,secondStdevEnd],y=[0,0.17],mode="lines",name="Standard Deviation Two End"))
fig.add_trace(go.Scatter(x=[thirdStdevStart,thirdStdevStart],y=[0,0.17],mode="lines",name="Standard Deviation Three Start"))
fig.add_trace(go.Scatter(x=[thirdStdevEnd,thirdStdevEnd],y=[0,0.17],mode="lines",name="Standard Deviation Three End"))
fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_score"].tolist()
mean2=statistics.mean(data)
print("Mean Of Data 2 ",mean2)
fig=ff.create_distplot([MeanList],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.20],mode="lines",name="mean2"))
fig.add_trace(go.Scatter(x=[firstStdevEnd,firstStdevEnd],y=[0,0.17],mode="lines",name="Standard Deviation One End"))
fig.add_trace(go.Scatter(x=[secondStdevEnd,secondStdevEnd],y=[0,0.17],mode="lines",name="Standard Deviation Two End"))
fig.add_trace(go.Scatter(x=[thirdStdevEnd,thirdStdevEnd],y=[0,0.17],mode="lines",name="Standard Deviation Three End"))
fig.show()
zscore=(mean2-mean)/stdev
print("Zscore Is ",zscore)


df=pd.read_csv("data3.csv")
data=df["Math_score"].tolist()
mean3=statistics.mean(data)
print("Mean Of Data 2 ",mean3)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig=ff.create_distplot([MeanList],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean3,mean3],y=[0,0.20],mode="lines",name="mean3"))
fig.add_trace(go.Scatter(x=[secondStdevEnd,secondStdevEnd],y=[0,0.17],mode="lines",name="Standard Deviation Two End"))
fig.add_trace(go.Scatter(x=[thirdStdevEnd,thirdStdevEnd],y=[0,0.17],mode="lines",name="Standard Deviation Three End"))
fig.show()
zscore=(mean3-mean)/stdev
print("Zscore Is ",zscore)