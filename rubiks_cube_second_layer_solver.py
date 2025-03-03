def solve_second_layer(cube):
    # Orient the top layer first
    orient_top_layer(cube)

    # Permute the top layer
    permute_top_layer(cube)

    # Final adjustment
    if cube.positions[0] == 1:
        cube.apply_move(["U'"])
    elif cube.positions[0] == 2:
        cube.apply_move(["U2"])
    elif cube.positions[0] == 3:
        cube.apply_move(["U"])


def apply_and_print(cube, moves):
    if not moves:
        return
    move_str = " ".join(moves)
    print(f"Applying: {move_str}")
    cube.apply_move(moves)


def check_and_align_oriented_corners(cube):
    # Set up the orientation in terms of positions, not corners
    upper_layer_positions = cube.positions[0:4]
    corner_in_position = []
    for i in range(4):
        corner_in_position.append(upper_layer_positions.index(i))
    print(f"Corners in position [0,1,2,3] are {corner_in_position}")
    layer_orientations = [cube.orientations[i] for i in corner_in_position]
    print(f"Layer orientation from 0 to 3 is {layer_orientations}")
    indices = [i for i in range(4) if layer_orientations[i] == 0]
    s = len(indices)

    # Check if it is already oriented
    if s == 4:
        return 4
    
    # Align the top layer for different cases
    elif s == 1:
        # Identify the piece with correct orientation
        current_position_of_correct_piece = indices
        print(f"Correct piece is at position {current_position_of_correct_piece}")

        # Align the piece with correct orientation
        if current_position_of_correct_piece == [0]:
            apply_and_print(cube, ["U2"])
            return "1corner"
        elif current_position_of_correct_piece == [1]:
            apply_and_print(cube, ["U"])
            return "1corner"
        elif current_position_of_correct_piece == [2]:
            return "1corner"
        elif current_position_of_correct_piece == [3]:
            apply_and_print(cube, ["U'"])
            return "1corner"
        else:
            print("Error: Invalid position of 1 correct piece.")
        
    elif s == 2:
        # Identify which case it is, neighboring or diagonal
        current_positions_of_correct_pieces = indices
        print(f"Correct pieces are at positions {current_positions_of_correct_pieces}")

        # If the two are next to each other
        if current_positions_of_correct_pieces == [0, 1]:
            apply_and_print(cube, ["U'"])
            return "2neighbor"
        elif current_positions_of_correct_pieces == [1, 2]:
            apply_and_print(cube, ["U2"])
            return "2neighbor"
        elif current_positions_of_correct_pieces == [2, 3]:
            apply_and_print(cube, ["U"])
            return "2neighbor"
        elif current_positions_of_correct_pieces == [3, 0]:
            return "2neighbor"
        
        # If the two are in diagonal positions
        elif current_positions_of_correct_pieces == [0, 2]:
            return "2diagonal"
        elif current_positions_of_correct_pieces == [1, 3]:
            apply_and_print(cube,["U"])
            return "2diagonal"
        else:
            print("Error: Invalid positions of 2 correct pieces.")
        
    elif s == 0:
        # Identify which case it is, a T or H shape

        # If it is the T shape    or [1,2,2,1] or [1,1,2,2,] or [2,1,1,2]
        if layer_orientations == [2,2,1,1]:
            return "Tshape"
        elif layer_orientations == [1,2,2,1]:
            cube.apply_move(["U'"])
            return "Tshape"
        elif layer_orientations == [1,1,2,2]:
            cube.apply_move(["U2"])
            return "Tshape"
        elif layer_orientations == [2,1,1,2]:
            cube.apply_move(["U"])
            return "Tshape"

        # If it is the H shape
        elif layer_orientations == [2,1,2,1]:
            return "Hshape"
        elif layer_orientations == [1,2,1,2]:
            cube.apply_move(["U"])
            return "Hshape"

    else:
        print("Error: Invalid number of correct pieces.")
    
def orient_top_layer(cube):
    # Orient the top layer
    print("Orienting top layer")
    case = check_and_align_oriented_corners(cube)
    upper_layer_positions = cube.positions[0:4]
    corner_in_position = []
    for i in range(4):
        corner_in_position.append(upper_layer_positions.index(i))
    layer_orientations = [cube.orientations[i] for i in corner_in_position]
    print(f"Layer orientation is: {layer_orientations}")

    if case == "1corner":
        # Check the orientations
        print("1 corner shows up, the cube is:\n", cube)
        if layer_orientations[0] == 1:
            apply_and_print(cube, ["R'","U'","R","U'","R'","U2","R"])
            print("After turning, the current cube is:\n", cube)
        elif layer_orientations[0] == 2:
            apply_and_print(cube, ["F","U","F'","U","F","U2","F'"])
            print("After turning, the current cube is:\n", cube)
        else:
            print("Error: Invalid case1.")

    elif case == "2neighbor":
        # The two are next to each other
        print("2 neighboring corners show up, the cube is:\n", cube)

        if layer_orientations[1] == 1:
            apply_and_print(cube, ["R","U","R'","U'","R'","F","R","F'"])
            print("After turning, the current cube is:\n", cube)
        elif layer_orientations[1] == 2:
            apply_and_print(cube, ["F","R","U","R'","U'","F'"])
            print("After turning, the current cube is:\n", cube)
        else:
            print("Error: Invalid case2neighbor.")
        
    elif case == "2diagonal":
        # The 2 are diagonal to each other
        print("2 diagonal corners show up, the cube is:\n", cube)

        if layer_orientations[1] == 1:
            apply_and_print(cube,["F","R","U'","R'","U'","R","U","R'","F'"])
            print("After turning, the current cube is:\n", cube)
        elif layer_orientations[1] == 2:
            apply_and_print(cube,["U2","F","R","U'","R'","U'","R","U","R'","F'"])
            print("After turning, the current cube is:\n", cube)
        else:
            print("Error: Invalid case2diagonal.")

    elif case == "Tshape":
        print("Tshape: The current cube is:\n", cube)
        apply_and_print(cube,["F","R","U","R'","U'","R","U","R'","U'","F'"])
        print("After turning, the cube is:\n", cube)

    elif case == "Hshape":
        print("Hshape: The current cube is:\n", cube)
        apply_and_print(cube,["R2","U2","R","U2","R2"])
        print("After turning, the cube is:\n", cube)

    elif case == 4:
        print("Top layer already oriented.")

    else:
        print("Error: None of the 4 case.")


def permute_top_layer(cube):

    # Align corner 0
    correct_corner = cube.positions[0]
    if correct_corner == 1:
        apply_and_print(cube,["U'"])
    elif correct_corner == 2:
        apply_and_print(cube,["U2"])
    elif correct_corner == 3:
        apply_and_print(cube,["U"])
    
    layer_positions = []
    for i in range(4):
        layer_positions.append(cube.positions.index(i))
        
    # There are 6 cases
    if layer_positions == [0,1,2,3]:
        print("Top layer already permuted.")
        print("The current cube is:", cube)

    elif layer_positions == [0,1,3,2]:
        apply_and_print(cube,["U", "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'", "U'"])
        print("The current cube is:", cube)

    elif layer_positions == [0,2,1,3]:
        apply_and_print(cube,["U2","R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'", "U2"])
        print("The current cube is:", cube)
    
    elif layer_positions == [0,2,3,1]:
        apply_and_print(cube,["R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'", "U"])
        print("The current cube is:", cube)
    
    elif layer_positions == [0,3,1,2]:
        apply_and_print(cube,["U'", "R", "U", "R'", "U'", "R'", "F", "R2", "U'", "R'", "U'", "R", "U", "R'", "F'", "U"])
        print("The current cube is:", cube)

    elif layer_positions == [0,3,2,1]:
        apply_and_print(cube,["F", "R", "U'", "R'", "U'", "R", "U", "R'", "F'", "R", "U", "R'", "U'", "R'", "F", "R", "F'","U2"])
        print("The current cube is:", cube)
    

