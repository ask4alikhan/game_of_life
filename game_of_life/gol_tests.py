from gol_functions import next_board_state as nb
import gol_functions

# TODO: Lots ore repeated code here, can we move this into reusable functions

if __name__ == "__main__":
    # Test 1: dead cells with no live neighbours
    # should stay dead.
    init_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    expected_next_state1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    actual_next_state1 = nb(init_state1)

    if expected_next_state1 == actual_next_state1:
        print("PASSED 1")
    else:
        print("FAILED 1!")
        print( "Expected:")
        print(expected_next_state1)
        print("Actual:")
        print(actual_next_state1)

    # Test 2: dead cells with exactly 3 neighours
    # should come alive.
    init_state2 = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0],
    ]
    expected_next_state2 = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0],
    ]
    actual_next_state2 = nb(init_state2)

    if expected_next_state2 == actual_next_state2:
        print("PASSED 2")
    else:
        print("FAILED 2!")
        print( "Expected:")
        print(expected_next_state2)
        print("Actual:")
        print(actual_next_state2)        
