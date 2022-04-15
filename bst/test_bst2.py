import unittest
from bst import BinarySearchTree

class BSTTestCase(unittest.TestCase):
    def setUp(self): 
        self.bst = BinarySearchTree()
        self.bst.add(20, "Value for 20")
        self.bst.add(22, "Value for 22")
        self.bst.add(15, "Value for 15")
        self.bst.add(28, "Value for 28")
        self.bst.add(1, "Value for 1")
        self.bst.add(4, "Value for 4")
        self.bst.add(5, "Value for 5")
        self.bst.add(6, "Value for 6")
    
    def test_add(self):
        bsTree = BinarySearchTree()
        self.assertEqual(bsTree.size(), 0)
        bsTree.add(25, "Value for 25")
        # Size of bsTree must be 1
        self.assertEqual(bsTree.size(), 1)
        bsTree.add(100, "Value for 100")
        # Size of bsTree must be 2
        self.assertEqual(bsTree.size(), 2)

        # The added keys must exist.
        self.assertEqual(bsTree.search(25), "Value for 25")
        self.assertEqual(bsTree.search(100), "Value for 100")

    def test_inorder(self):
        """
        tests for inorder_walk
        """
        actual_output = self.bst.inorder_walk()
        expected_output =  [1, 4, 5, 6, 15, 20, 22, 28] 

        self.assertListEqual(actual_output, expected_output)

        # Add one node
        self.bst.add(25, "Value for 25")
        # Inorder traversal must return a different sequence
        self.assertListEqual(self.bst.inorder_walk(),  [1, 4, 5, 6, 15, 20, 22,25, 28] )

    def test_postorder(self):
        """
        tests for postorder_walk
        """
        actual_output = self.bst.postorder_walk()
        expected_output = [6, 5, 4, 1, 15, 28, 22, 20]
        
        self.assertListEqual(actual_output, expected_output)

        # Add one node
        self.bst.add(25, "Value for 25")
        # Postorder traversal must return a different sequence
        self.assertListEqual(self.bst.postorder_walk(), [6, 5, 4, 1, 15, 25, 28, 22, 20])

    def test_preorder(self):
        """
        tests for preorder_walk
        """
        self.assertListEqual(self.bst.preorder_walk(), [20, 15, 1, 4, 5, 6, 22, 28])

        # Add one node
        self.bst.add(25, "Value for 25")
        # Preorder traversal must return a different sequence
        self.assertListEqual(self.bst.preorder_walk(), [20, 15, 1, 4, 5, 6, 22, 28, 25])
    
    def test_search(self):
        """
        tests for search
        """
        actual_output = self.bst.search(15)
        expected_output = "Value for 15"
        self.assertEqual(actual_output, expected_output)
    
        self.assertFalse(self.bst.search(90))

        self.bst.add(90, "Value for 90")
        self.assertEqual(self.bst.search(90), "Value for 90")

    def test_remove(self):
        """
        tests for remove
        """
        self.bst.remove(40)
        
        self.assertEqual(self.bst.size(), 8)
        self.assertListEqual(self.bst.inorder_walk(), [1, 4, 5, 6, 15, 20, 22, 28])
        self.assertListEqual(self.bst.preorder_walk(), [20, 15, 1, 4, 5, 6, 22, 28])

    def test_smallest(self):
        """
        tests for smallest
        """
        self.assertTupleEqual(self.bst.smallest(), (1, "Value for 1"))

        # Add some nodes
        self.bst.add(6, "Value for 6")
        self.bst.add(4, "Value for 4")
        self.bst.add(0, "Value for 0")
        self.bst.add(32, "Value for 32")

        # Now the smallest key is 0.
        self.assertTupleEqual(self.bst.smallest(), (0, "Value for 0"))

    def test_largest(self):
        """
        tests for largest
        """
        self.assertTupleEqual(self.bst.largest(), (28, "Value for 28"))

        # Add some nodes
        self.bst.add(6, "Value for 6")
        self.bst.add(54, "Value for 54")
        self.bst.add(0, "Value for 0")
        self.bst.add(32, "Value for 32")

        # Now the largest key is 54
        self.assertTupleEqual(self.bst.largest(), (54, "Value for 54"))

if __name__ == "__main__":
    unittest.main()    