
class Node:
    def __init__(self) -> None:
        self.key =None
        self.value = None
        self.left = None
        self.right = None
    
    


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.__size = 0
    


    def add(self,key,value):
        if self.root == None:
            self.root = Node()
            self.root.key = key
            self.root.value = value
            self.__size +=1
  
        else:
            newNode = self.root

            while(newNode!=None):
             
                temp = newNode
                if newNode.key> key:
             
                
                    newNode = newNode.left

                elif newNode.key < key:
                   
                    
                    newNode = newNode.right
                
                else:
                    # print('found existing key so updatig')#for handling update case while same key present in tree is sent


                    break

        
            if temp.key > key:
                temp.left = Node()
                newNode = temp.left 
                newNode.value = value
                newNode.key = key
                self.__size += 1
            
            elif temp.key < key:
                temp.right = Node()
                newNode = temp.right
                newNode.value = value
                newNode.key = key
                self.__size += 1
            
            else:
                temp.value = value #for handling update case while same key present in tree is sent
        
    def size(self):
            return self.__size
    
    def search(self,key):
        newNode = self.root
        
        while(newNode!=None):
     
            if newNode.key == key:
                return newNode.value
            elif newNode.key > key:
                newNode=newNode.left 
            
            else:
                newNode = newNode.right
        
        return False

    def smallest(self):
         
        return self._smallest(self.root)


    
    def _smallest(self,rootnode):
        while rootnode.left != None :
            rootnode =rootnode.left 
        return (rootnode.key,rootnode.value)


    def largest(self):
        newNode = self.root 
        while newNode.right != None :
         
            newNode = newNode.right
        
        return (newNode.key,newNode.value)
    


    
    def inorder_walk(self):
        inorder_walk_list = []

        self.Call_inorder_walk(self.root,inorder_walk_list)
        return inorder_walk_list
    
    
    def Call_inorder_walk(self,root,in_list):
        if not root:
            return
        else:
            self.Call_inorder_walk(root.left,in_list)
            in_list.append(root.key)
            self.Call_inorder_walk(root.right,in_list)
    
    def preorder_walk(self):
        preorder_walk_list = []
        root_node = self.root
        self.Call_preorder_wlak(root_node,preorder_walk_list)
        return preorder_walk_list
    
    def Call_preorder_wlak(self,root,pre_list):
        if not root:
            return 
        else:
            pre_list.append(root.key)
            self.Call_preorder_wlak(root.left,pre_list)
            self.Call_preorder_wlak(root.right,pre_list)

    def postorder_walk(self):
        postorder_walk_list = []
        root_node = self.root
        self.Call_postorder_wlak(root_node,postorder_walk_list)
        return postorder_walk_list
    
    def Call_postorder_wlak(self,root,pre_list):
        if not root:
            return 
        else:
            
            self.Call_postorder_wlak(root.left,pre_list)
            self.Call_postorder_wlak(root.right,pre_list)
            pre_list.append(root.key)


    def remove(self,delkey):
        
        if self.search(delkey)==False:
            return False
        self.root = self.Call_remove(self.root,delkey)
        self.__size -= 1
    
    def Call_remove(self,node,delkey):
        if node == None:
            return node
        elif delkey < node.key:
            node.left  = self.Call_remove(node.left,delkey)
            return node
        elif delkey > node.key:
            node.right = self.Call_remove(node.right,delkey)
            return node

        else:
            if node.left == None and node.right == None:
                return None 

            elif node.left == None or node.right == None:
                if node.left is not None :
                    return node.left
                
                else:
                    return node.right
                
            
            else:
                successor =self._smallest(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right = self.Call_remove(node.right,successor.key)
                return node 


        
bsTree = BinarySearchTree()
print(bsTree.size())
