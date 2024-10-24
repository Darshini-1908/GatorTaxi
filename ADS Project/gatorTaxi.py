import sys

from ride_model import Ride
from min_heap import MinHeap
from min_heap import MinHeapNode
from reb_black_tree import RedBlackTree, RBTNode

# This function adds a new ride to the system, represented by a min heap and a red-black tree.
def r_Ride(ride, heap, rbt):
    if rbt.get_ride(ride.rNumb) is not None:
        # If the ride already exists, add an error message to the output and exit the program.
        addOutput(None, "Duplicate rNumb", False)
        sys.exit(0)
        return
    rbt_node = RBTNode(None, None)
    min_heap_node = MinHeapNode(ride, rbt_node, heap.curr_size + 1)
    heap.insert(min_heap_node)
    rbt.insert(ride, min_heap_node)


def addOutput(ride, msge, lst):
    #opens the file "output.txt" in "append" mode
    file = open("output.txt", "a")
    if ride is None:
        file.write(msge + "\n")
    else:
        msge = ""
        if not lst:
            msge += ("(" + str(ride.rNumb) + "," + str(ride.rCost) + "," + str(ride.duration_of_trip) + ")\n")
        else:
            if len(ride) == 0:
                msge += "(0,0,0)\n"
            for i in range(len(ride)):
                if i != len(ride) - 1:
                    msge = msge + ("(" + str(ride[i].rNumb) + "," + str(ride[i].rCost) + "," + str(
                        ride[i].duration_of_trip) + "),")
                else:
                    msge = msge + ("(" + str(ride[i].rNumb) + "," + str(ride[i].rCost) + "," + str(
                        ride[i].duration_of_trip) + ")\n")
#the function adds a message to indicating that there were no rides: "(0,0,0)\n"
        file.write(msge)
    file.close()

## This function takes in a ride number and a RideBookingSystem object as inputs.
def r_Print(rNumb, rbt):
    res = rbt.get_ride(rNumb)
    # If there is no ride with the given ride number, add a message to the output indicating so.
    if res is None:
        addOutput(Ride(0, 0, 0), "", False)
    else:
        addOutput(res.ride, "", False)


def r_Prints(l, h, rbt):
    ## Get the list of rides that fall within the given range.
    lst = rbt.get_rides_in_range(l, h)
    addOutput(lst, "", True)


def nxtRide_get(heap, rbt):
    # Check if the heap is not empty.
    if heap.curr_size != 0:
        popped_node = heap.pop()
        rbt.delete_node(popped_node.ride.rNumb)
        # Add the popped ride to the output.
        addOutput(popped_node.ride, "", False)
    else:
        addOutput(None, "No active ride requests", False)


def rideCancel(ride_number, heap, rbt):
    heap_node = rbt.delete_node(ride_number)
    # Delete ride node corresponding to ride number from tree to get the corresponding heap node.
    if heap_node is not None:
        heap.removeEle(heap_node.min_heap_index)


def updteRide(rNumb, new_duration, heap, rbt):
    #Get the ride node corresponding to the ride number from the tree.
    rbt_node = rbt.get_ride(rNumb)
    if rbt_node is None:
        print("")
    elif new_duration <= rbt_node.ride.duration_of_trip:
        heap.upgradeEle(rbt_node.min_heap_node.min_heap_index, new_duration)
    elif rbt_node.ride.duration_of_trip < new_duration <= (2 * rbt_node.ride.duration_of_trip):
        rideCancel(rbt_node.ride.rNumb, heap, rbt)
        r_Ride(Ride(rbt_node.ride.rNumb, rbt_node.ride.rCost + 10, new_duration), heap, rbt)
        # If the new duration is more than twice the current duration, cancel the ride.
    else:
        rideCancel(rbt_node.ride.rNumb, heap, rbt)


if __name__ == "__main__":
    heap = MinHeap()
    rbt = RedBlackTree()
    file = open("output.txt", "w")
    file.close()
    file = open("input.txt", "r")
    for tmp in file.readlines():
        numIn = []
        for num in tmp[tmp.index("(") + 1:tmp.index(")")].split(","):
            if num != '':
                numIn.append(int(num))
                #Loop through each line of the input file and extract the numbers enclosed in parentheses.
        if "Insert" in tmp:
            r_Ride(Ride(numIn[0], numIn[1], numIn[2]), heap, rbt)
        elif "Print" in tmp:
            if len(numIn) == 1:
                r_Print(numIn[0], rbt)
            elif len(numIn) == 2:
                r_Prints(numIn[0], numIn[1], rbt)
        elif "UpdateTrip" in tmp:
            updteRide(numIn[0], numIn[1], heap, rbt)
        elif "GetNextRide" in tmp:
            nxtRide_get(heap, rbt)
        elif "CancelRide" in tmp:
            rideCancel(numIn[0], heap, rbt)#Print r_Print or r_Prints to print the requested ride information to the output file.

