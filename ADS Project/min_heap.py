class MinHeap:
    def __init__(self):
        self.heap_lst = [0]
        self.curr_size = 0

    def insert(self, ele):
        self.heap_lst.append(ele)
        self.curr_size += 1
        self.heapUpward(self.curr_size)

#index dr, restores the heap property by swapping with its parent 
    def heapUpward(self, dr):
        while (dr // 2) > 0:
            if self.heap_lst[dr].ride.less_than(self.heap_lst[dr // 2].ride):
                self.swap(dr, (dr // 2))
            else:
                break
            dr = dr // 2

    def swap(self, ind1, ind2):
        temp = self.heap_lst[ind1]
        self.heap_lst[ind1] = self.heap_lst[ind2]
        self.heap_lst[ind2] = temp
        self.heap_lst[ind1].min_heap_index = ind1
        self.heap_lst[ind2].min_heap_index = ind2

    def heapDownward(self, dr):
        while (dr * 2) <= self.curr_size:
            ind = self.childMin_Indx(dr)
            if not self.heap_lst[dr].ride.less_than(self.heap_lst[ind].ride):
                self.swap(dr, ind)
            dr = ind

#returns the index of its smallest child.
    def childMin_Indx(self, dr):
        if (dr * 2) + 1 > self.curr_size:
            return dr * 2
        else:
            if self.heap_lst[dr * 2].ride.less_than(self.heap_lst[(dr * 2) + 1].ride):
                return dr * 2
            else:
                return (dr * 2) + 1

    def upgradeEle(self, dr, new_sol):
        node = self.heap_lst[dr]
        node.ride.duration_of_trip = new_sol
        if dr == 1:
            self.heapDownward(dr)
        elif self.heap_lst[dr // 2].ride.less_than(self.heap_lst[dr].ride):
            self.heapDownward(dr)
        else:
            self.heapUpward(dr)

#emoves the element at index dr and restores the heap property by swapping with its smallest child
    def removeEle(self, dr):

        self.swap(dr, self.curr_size)
        
        self.curr_size -= 1
        *self.heap_lst, _ = self.heap_lst

        self.heapDownward(dr)

#Removes and returns the smallest element in the heap.
    def pop(self):

        if len(self.heap_lst) == 1:
            return 'No Rides Available'

        root = self.heap_lst[1]

        self.swap(1, self.curr_size)
       
        self.curr_size -= 1
        *self.heap_lst, _ = self.heap_lst

        self.heapDownward(1)

        return root


class MinHeapNode:
    def __init__(self, ride, rbt, min_heap_index):
        self.ride = ride
        self.rbTree = rbt
        self.min_heap_index = min_heap_index
