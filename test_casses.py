"""
All test cases for Sudoku

Boundry Tests:
    Location Input Tests:

    Test input c10
    expected output: Error

    Test Input J2
    expected Output: Error

    Test input 1
    expected Output: Error

    Test input a
    expected Output: Error

    Test input c2
    expected Output: Request for value

    Value Input Boundry Tests:

    Test input a
    expected Output: Error

    Test Input 10
    expected Output: Error

    Test input 1
    expected Output: Updated Board

    Test input c2, .1
    expected Output: Error, please enter a full number between 0-9

requirement Tests:
    Test input C3, 3
    expected Output: space is full, due to column

    Test input C3, 5
    expected Output: invalid input, row check

    Test input C3, 5
    expected Output: invalid input, Square check

    Test input 'T' 
    expected Output: Invalid input, try again

    Test input b2
    expected output: success, lowercase letter

    Test input 2b
    expected output: Success, out of order

    Test input: B20
    expected Output: Invalid input

    Test input C1
    expected Output: Square is full

    Test input P, C2
    expected Output: 1, 5, 9

    Test input: C3, 1
    expeted output: sqare is full

Error Testing:
    Test input Get_Board(Easy.json) #You can use any file that you don't have a board in
    expected output: error, file not found

    Test input Get_Board(Tic_Tac_toe.json)
    expected output: board configuration invalid
    



"""