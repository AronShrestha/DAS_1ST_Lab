import random
from searchingAlgo import binary__Search,linear_Search
import matplotlib.pyplot as plt
import time
import pandas as pd  



def time_taken(searchingAlgo,*args):
    """This function takes which searching algorithm to  use and it's respective algorithm parameters"""
    time1 = time.time()
    t11=searchingAlgo(*args)
    time2 = time.time()
    return ((time2-time1))

def Searching():
    """This function creates dictionary to store execution time and step size of given search algorithm """
    records ={'BestCase_linear':[],'WorstCase_linear':[],'BestCase_Binary':[],'WorstCase_Binary':[],'size':[]}
    for i in range(10,100000,5000):
        
        sampleLinear = random.sample(range(100000),i)
        sampleBinary = list(range(i))
        records['BestCase_linear'].append(time_taken(linear_Search,sampleLinear,sampleLinear[0]))
        records['WorstCase_linear'].append(time_taken(linear_Search,sampleLinear,sampleLinear[-1]))
        records['BestCase_Binary'].append(time_taken(binary__Search,sampleBinary,sampleBinary[(i-1)//2],0,len(sampleBinary)))
        records['WorstCase_Binary'].append(time_taken(binary__Search,sampleBinary,sampleBinary[-1],0,len(sampleBinary)))
        records['size'].append(i)
    

    return records
        



def plotGraph(data):
    """This function plots the data ,data is dictionary that has executio time and size of inputs"""
 
    df = pd.DataFrame.from_dict(data)
    fig, (graph_linear,graph_binary) = plt.subplots(2)
    graph_linear.set_title('Linear Search')
    
    graph_linear.set_xlabel('Size of data')
    graph_linear.set_ylabel('Execution time')
 
    graph_linear.plot(df['size'],df['WorstCase_linear'],label='Worstcase_LinearSearch')
    graph_linear.plot(df['size'],df['BestCase_linear'],label='Worstcase_LinearSearch')
    graph_linear.legend()
    
    graph_binary.set_title('Binary Search')
    graph_binary.set_xlabel('Size of data')
    graph_binary.set_ylabel('Execution time')
    graph_binary.plot(df['size'],df['WorstCase_Binary'],label='WorstCase_BinarySearch')
    graph_binary.plot(df['size'],df['BestCase_Binary'],label='BestCase_BinarySearch')
    
    graph_binary.legend()
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    datas = Searching()
    plotGraph(datas)
