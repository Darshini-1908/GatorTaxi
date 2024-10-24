class RBTNode:
    def __init__(self, ride, min_heap_node):
        self.ride = ride
        self.parent = None  # parent node
        self.left = None  # left node
        self.right = None  # right node
        self.color = 1  # 1=red , 0 = black
        self.min_heap_node = min_heap_node


class RedBlackTree:
    def __init__(self):
        self.null_node = RBTNode(None, None)
        self.null_node.left = None
        self.null_node.right = None
        self.null_node.color = 0
        self.root = self.null_node

    #defines the get_ride method for a Red-Black Tree class
    def get_ride(self, sol):
        temp = self.root

       
        while temp != self.null_node:
            if temp.ride.rNumb == sol:
                return temp
            if temp.ride.rNumb < sol:
                temp = temp.right
            else:
                temp = temp.left

        return None

    
    def deletedTreeAfter(self, node):
        ## loop until we have traversed up to the root or until the node is not a red node
        while node != self.root and node.color == 0:
            if node == node.parent.right:
                childParent = node.parent.left
                if childParent.color != 0:
                    node.parent.color = 1
                    childParent.color = 0
                    self.rotationRight(node.parent)
                    childParent = node.parent.left

                if childParent.right.color == 0 and childParent.left.color == 0:
                    childParent.color = 1
                    node = node.parent
                else:
                    if childParent.left.color != 1:
                        childParent.right.color = 0
                        childParent.color = 1
                        self.rotationLeft(childParent)
                        childParent = node.parent.left

                    childParent.color = node.parent.color
                    node.parent.color = 0
                    childParent.left.color = 0
                    self.rotationRight(node.parent)
                    node = self.root
                    #We set the sibling of the node as the right child of the parent of the node
            else:
                childParent = node.parent.right
                if childParent.color != 0:
                    node.parent.color = 1
                    childParent.color = 0
                    self.rotationLeft(node.parent)
                    childParent = node.parent.right

                if childParent.right.color == 0 and childParent.left.color == 0:
                    childParent.color = 1
                    node = node.parent
                else:
                    if childParent.right.color != 1:
                        childParent.left.color = 0
                        childParent.color = 1
                        self.rotationRight(childParent)
                        childParent = node.parent.right

                    childParent.color = node.parent.color
                    node.parent.color = 0
                    childParent.right.color = 0
                    self.rotationLeft(node.parent)
                    node = self.root

        node.color = 0

#The node to be replaced is node and the node that replaces it is child_node.
    def __rb_transplant(self, node, child_node):
        if node.parent is None:
            self.root = child_node
        elif node == node.parent.right:
            node.parent.right = child_node
        else:
            node.parent.left = child_node
        child_node.parent = node.parent

#delete_node variable is initialized to a null node, which will be used to store the node to be deleted.
    def nodeDeleter(self, node, sol):
        delete_node = self.null_node
        while node != self.null_node:
            if node.ride.rNumb == sol:
                delete_node = node
            if node.ride.rNumb >= sol:
                node = node.left
            else:
                node = node.right
#variable y is initialized to delete_node, and its original color is stored in y_original_color
        if delete_node == self.null_node:
            return
        heap_node = delete_node.min_heap_node
        y = delete_node
        y_original_color = y.color
        if delete_node.left == self.null_node:
            x = delete_node.right
            self.__rb_transplant(delete_node, delete_node.right)
        elif (delete_node.right == self.null_node):
            x = delete_node.left
            self.__rb_transplant(delete_node, delete_node.left)
        else:
            y = self.minimum(delete_node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == delete_node:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = delete_node.right
                y.right.parent = y

            self.__rb_transplant(delete_node, y)
            y.left = delete_node.left
            y.left.parent = y
            y.color = delete_node.color
        if y_original_color == 0:
            self.deletedTreeAfter(x)

        return heap_node

    def treeAfterInsert(self, tmpNode):
        while tmpNode.parent.color == 1:
            if tmpNode.parent == tmpNode.parent.parent.left:
                childParent = tmpNode.parent.parent.right
# If the sibling is black or None, perform necessary rotations and color changes
                if childParent.color == 0:
                    if tmpNode == tmpNode.parent.right:
                        tmpNode = tmpNode.parent
                        self.rotationLeft(tmpNode)
                    tmpNode.parent.color = 0
                    tmpNode.parent.parent.color = 1
                    self.rotationRight(tmpNode.parent.parent)
                else:
                    childParent.color = 0
                    tmpNode.parent.color = 0
                    tmpNode.parent.parent.color = 1
                    tmpNode = tmpNode.parent.parent

            else:
                childParent = tmpNode.parent.parent.left
                if childParent.color == 0:
                    if tmpNode == tmpNode.parent.left:
                        tmpNode = tmpNode.parent
                        self.rotationRight(tmpNode)
                    tmpNode.parent.color = 0
                    tmpNode.parent.parent.color = 1
                    self.rotationLeft(tmpNode.parent.parent)
                else:
                    childParent.color = 0
                    tmpNode.parent.color = 0
                    tmpNode.parent.parent.color = 1
                    tmpNode = tmpNode.parent.parent
# If reached the root node, exit the loop
            if tmpNode == self.root:
                break
        self.root.color = 0

#res is a list that holds the Ride objects that fall within the specified range.
    def inRangeRides(self, node, low, high, res):
        if node == self.null_node:
            return

        if low < node.ride.rNumb:
            self.inRangeRides(node.left, low, high, res)
        if low <= node.ride.rNumb <= high:
            res.append(node.ride)
        self.inRangeRides(node.right, low, high, res)

    def get_rides_in_range(self, low, high):
        res = []
        self.inRangeRides(self.root, low, high, res)
        return res

    def minimum(self, node):
        while node.left != self.null_node:
            node = node.left
        return node

    def rotationLeft(self, l):
        #The function assigns the right child of l as m
        m = l.right
        l.right = m.left
        if m.left != self.null_node:
            m.left.parent = l

        m.parent = l.parent
        if l.parent == None:
            self.root = m
        elif l == l.parent.left:
            l.parent.left = m
        else:
            l.parent.right = m
        m.left = l
        l.parent = m#The parent of l is updated to m

    def rotationRight(self, l):
        #The function first saves the left child of node l in variable m
        m = l.left
        l.left = m.right
        if m.right != self.null_node:
            m.right.parent = l

        m.parent = l.parent
        if l.parent == None:
            self.root = m
        elif l == l.parent.right:
            l.parent.right = m
        else:
            l.parent.left = m
        m.right = l
        l.parent = m

#a new RBTNode object is created with the given ride and min_heap object, and its attributes are set. 
    def insert(self, ride, min_heap):
        node = RBTNode(ride, min_heap)
        node.parent = None
        node.left = self.null_node
        node.right = self.null_node
        node.color = 1

        insertion_node = None
        temp_node = self.root

        while temp_node != self.null_node:
            insertion_node = temp_node
            if node.ride.rNumb < temp_node.ride.rNumb:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        node.parent = insertion_node
        if insertion_node is None:
            self.root = node
        elif node.ride.rNumb > insertion_node.ride.rNumb:
            insertion_node.right = node
        else:
            insertion_node.left = node

        if node.parent is None:
            node.color = 0
            return

        if node.parent.parent is None:
            return

        self.treeAfterInsert(node)

    def delete_node(self, rNumb):
        return self.nodeDeleter(self.root, rNumb)
