import random
from searchingAlgo import binary__Search,linear_Search
import matplotlib.pyplot as plt
import time
import pandas as pd  



def time_taken(searchingAlgo,*args):
    time1 = time.time()
    t11=searchingAlgo(*args)
    time2 = time.time()
    return ((time2-time1)*10**6)


def Searching():
    records ={'BestCase_linear':[],'WorstCase_linear':[],'BestCase_Binary':[],'WorstCase_Binary':[],'size':[]}
    for i in range(1000,100000,5000):
        
        sampleLinear = random.sample(range(100000),i)
        sampleBinary = list(range(i))
        records['BestCase_linear'].append(time_taken(linear_Search,sampleLinear,sampleLinear[0]))
        records['WorstCase_linear'].append(time_taken(linear_Search,sampleLinear,sampleLinear[-1]))
        records['BestCase_Binary'].append(time_taken(binary__Search,sampleBinary,sampleBinary[(i-1)//2],0,len(sampleBinary)))
        records['WorstCase_Binary'].append(time_taken(binary__Search,sampleBinary,sampleBinary[-1],0,len(sampleBinary)))
        records['size'].append(i)


    plotGraph(records)
        




def plotGraph(data):
    print("hello")
    df = pd.DataFrame.from_dict(data)
    fig, (graph_linear,graph_binary) = plt.subplots(2)
 
    graph_linear.plot(df['BestCase_linear'],df['size'])
    graph_binary.plot(df['BestCase_Binary'],df['size'])

Searching()