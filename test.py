import unittest
from searchingAlgo import linear_Search,binary__Search

class Search(unittest.TestCase):
    '''This class uses built-in python unittest to test tour searching algorithm'''
    def test_linear_Search(self):
        '''Test case for Linear search'''
        List= [12,13,4,1,25,3]
        self.assertEqual(linear_Search(List,12),0)
        self.assertEqual(linear_Search(List,1),3)
        self.assertEqual(linear_Search(List,13),1)
        self.assertEqual(linear_Search(List,3),5)
        self.assertEqual(linear_Search(List,25),4)
        self.assertEqual(linear_Search(List,4),2)
        self.assertEqual(linear_Search(List,0),-1)
        

    def test_binary_Search(self):
        '''Test case for Binary search'''
        List =[1,2,3,44,55,66,88,999]
        self.assertEqual(binary__Search(List,target=1,low=0,high=len(List)),0)
        self.assertEqual(binary__Search(List,target=2,low=0,high=len(List)),1)
        self.assertEqual(binary__Search(List,target=88,low=0,high=len(List)),6)
        self.assertEqual(binary__Search(List,target=999,low=0,high=len(List)),7)
        self.assertEqual(binary__Search(List,target=55,low=0,high=len(List)),4)
        self.assertEqual(binary__Search(List,target=100,low=0,high=len(List)),-1)

if __name__=="__main__":
    unittest.main()

