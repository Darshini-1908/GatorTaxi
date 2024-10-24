# GatorTaxi Project

## Overview

GatorTaxi is a ride-sharing service implementation that simulates the behavior of managing ride requests using various data structures and algorithms. This project involves inserting, updating, and retrieving ride details based on given operations. It supports functionalities like adding new ride requests, fetching the next available ride, updating ride details, and printing the state of active rides.

## Files

### 1. `gatorTaxi.py`
The main script implementing the GatorTaxi service. It integrates various modules and classes to manage ride requests and perform operations like:
- `Insert(rNumb, x, y)`: Adds a new ride request.
- `GetNextRide()`: Fetches the next ride based on priority.
- `UpdateTrip(rNumb, newTrip)`: Updates an existing ride with new trip details.
- `Print(a, b)`: Prints all ride requests within a specific range.
- `CancelRide(rNumb)`: Cancels a specific ride request.

### 2. `min_heap.py`
This module contains the implementation of a min-heap data structure. It is used for efficiently managing ride requests based on their priority to quickly retrieve the next ride. The min-heap supports operations like:
- Insertion of new elements (ride requests).
- Extraction of the minimum element (next ride).
- Deletion and updating of rides.

### 3. `reb_black_tree.py`
This module provides an implementation of a Red-Black Tree, a balanced binary search tree, to manage rides efficiently. It supports:
- Insertion of rides.
- Deletion and modification of nodes.
- Searching and printing ride requests within a range.

### 4. `ride_model.py`
This script defines the data model for rides, encapsulating attributes like ride number, start location, end location, and trip duration. The ride model is used throughout the system to create and manipulate ride objects consistently.

### 5. `input.txt`
This file contains a list of commands and inputs used to test the GatorTaxi system. Examples of commands include:
- `Insert(25,98,46)`: Adds a ride with ID 25 and start/end points (98, 46).
- `GetNextRide()`: Retrieves the next available ride.
- `UpdateTrip(53,15)`: Updates ride 53 with a new trip duration.
  
A full set of operations can be found in the file for testing various functionalities of the system.

### 6. `output.txt`
The output generated after executing the commands in `input.txt`. It displays the state of the system after each operation, showing results like the next ride fetched, the list of active rides, and errors such as duplicate ride numbers.

## Usage

1. Run the `gatorTaxi.py` script.
2. The program reads commands from `input.txt` and performs operations as described.
3. The output will be displayed in the console and can be saved to `output.txt`.

## Dependencies

- Python 3.x
- No additional external libraries are required.

## Notes

- Make sure that all modules (`min_heap.py`, `reb_black_tree.py`, `ride_model.py`) are in the same directory as `gatorTaxi.py` for proper integration.
- The `input.txt` file should be formatted correctly according to the accepted commands.

## Testing

To test the functionality, you can modify `input.txt` with different commands or use new input files to check various scenarios. The system will respond according to the defined behavior and constraints.

