from sorting import insertion_sort,Merge_sort
import matplotlib.pyplot as plt
import random,time
import pandas as pd

def execution_time(sorting_algo,*args):

    t1=time.time()
    sorting_algo(*args)
    t2 = time.time()
    return ((t2-t1))

def datas():
    data = {'InsertionWorst' :[],'InsertionBest' : [],'MergeSortWorst':[],'MergeSortBest':[],'size':[] }
    for i in range(0,10000,500):
        sample = random.sample(range(10000),i)
        sampleBest = sorted(sample) #returns sorted array bt sample remains same
        sampleWorst = sorted(sample)[::-1]
        data['size'].append(i)
        #for  insertionsort
        data['InsertionBest'].append(execution_time(insertion_sort,sampleBest))
        data['InsertionWorst'].append(execution_time(insertion_sort,sampleWorst))
        #for mergeSort
        data['MergeSortWorst'].append(execution_time(Merge_sort,sampleBest,0,i-1))
        data['MergeSortBest'].append(execution_time(Merge_sort,sampleWorst,0,i-1))
    return data

def plotGraph(data):
    """This function plots the data ,data is dictionary that has executio time and size of inputs"""
    df = pd.DataFrame.from_dict(data)
    fig, (graph_Insertion,graph_Merge) = plt.subplots(2)
    graph_Insertion.set_title('Insertion Sort')  
    graph_Insertion.set_xlabel('Size of data')
    graph_Insertion.set_ylabel('Execution time')
    graph_Insertion.plot(df['size'],df['InsertionWorst'],label='Worstcase_InsertionSort')
    graph_Insertion.plot(df['size'],df['InsertionBest'],label='Bestcase_InsertionSort')
    graph_Insertion.legend() 
    graph_Merge.set_title('Merge Sort')
    graph_Merge.set_xlabel('Size of data')
    graph_Merge.set_ylabel('Execution time')
    graph_Merge.plot(df['size'],df['MergeSortWorst'],label='WorstCase_MergeSort')
    graph_Merge.plot(df['size'],df['MergeSortBest'],label='BestCase_MergeSort')  
    graph_Merge.legend()
    plt.tight_layout()
    plt.show()

if __name__=='__main__':
    PlotData = datas()
    plotGraph(PlotData)

