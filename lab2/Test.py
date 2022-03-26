import unittest

from cv2 import merge

from sorting import insertion_sort,Merge,Merge_sort

class SortingTestCase(unittest.TestCase):
    unsorted_list = [0,6,5,4,3,2,1,7,8,9]
    sorte_list = [0,1,2,3,4,5,6,7,8,9]
    merg1 = [2,1]
    merge2 = [8,9,2,6]

    def test_insertion_sort(self):
        self.assertListEqual(insertion_sort(self.unsorted_list),self.sorte_list)
        self.assertListEqual(insertion_sort(self.sorte_list[::-1]),self.sorte_list)
        self.assertListEqual(insertion_sort(self.sorte_list),self.sorte_list)
    
    def test_merge(self):
        self.assertListEqual(Merge(self.merg1,0,0,1),[1,2])
        self.assertListEqual(Merge(self.merge2,0,1,3),[2,6,8,9])
    
    def test_merge_sort(self):
        self.assertListEqual(Merge_sort(self.unsorted_list,0,9),self.sorte_list)
        self.assertListEqual(Merge_sort(self.sorte_list,0,9),self.sorte_list)
        self.assertListEqual(Merge_sort(self.sorte_list[::-1],0,9),self.sorte_list)
    


if __name__=='__main__':
    unittest.main()