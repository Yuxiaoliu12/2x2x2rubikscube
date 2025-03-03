def apply_and_print(cube, moves):
    if not moves:
        return
    move_str = " ".join(moves)
    print(f"Applying: {move_str}")
    cube.apply_move(moves)

def solve_first_layer(cube):
    """
    Solve the first (bottom) layer of the cube.
    This focuses on solving the four bottom corners: BFR(4), BFL(5), BBL(6), BBR(7)
    """
    solve_corner(cube, 4)

    solve_corner(cube, 5)

    solve_corner(cube, 6)

    solve_corner(cube, 7)

def solve_corner(cube, target_position):
    """
    Solve a specific corner of the bottom layer.
    
    Args:
        cube: The Cube object
        target_position: The position to solve (4, 5, 6, or 7)
    """
    # First, find where the target piece is currently located
    target_piece = target_position  # The piece we want to solve
    current_position = cube.positions[target_piece]
    
    print(f"Solving corner {target_piece} (currently at position {current_position})")
    
    # If the piece is already correctly placed and oriented, we're done
    if current_position == target_position and cube.orientations[target_piece] == 0:
        print(f"Corner {target_piece} is already solved!")
        return
    
    # Step 1: If the piece is in the bottom layer but not in the correct position or orientation,
    # move it to the top layer without disturbing other solved corners
    if current_position in [4, 5, 6, 7]:
        if current_position == 4:  # BFR position
            apply_and_print(cube, ["R", "U", "R'"])
        elif current_position == 5:  # BFL position
            apply_and_print(cube, ["F", "U", "F'"])
        elif current_position == 6:  # BBL position
            apply_and_print(cube, ["L", "U", "L'"])
        elif current_position == 7:  # BBR position
            apply_and_print(cube, ["B", "U", "B'"])
        
        # After moving to the top layer, find the new position
        current_position = cube.positions[target_piece]
    
    # Step 2: Now the piece is in the top layer. Align it above its target position
    moves_to_align = get_alignment_moves(current_position, target_position)
    if moves_to_align:
        apply_and_print(cube, moves_to_align)
    
    # Get the current position and orientation after alignment
    current_position = cube.positions[target_piece]
    current_orientation = cube.orientations[target_piece]
    
    # Step 3: Insert the corner with the correct orientation based on its current state
    insertion_moves = get_insertion_moves(target_position, current_orientation)
    apply_and_print(cube, insertion_moves)
    current_position = cube.positions[target_piece]
    current_orientation = cube.orientations[target_piece]

    # Verify the corner is solved
    if cube.positions[target_piece] == target_position and cube.orientations[target_piece] == 0:
        print(f"Corner {target_piece} is now solved!")
    else:
        print(f"Warning: Corner {target_piece} is not solved correctly. Current position: {cube.positions[target_piece]}, orientation: {cube.orientations[target_piece]}")

def get_alignment_moves(current_position, target_position):
    """
    Get moves to align a piece in the top layer with its target position in the bottom layer
    """
    # Map of top positions to their corresponding bottom positions
    top_to_bottom = {
        0: 4,  # TFR -> BFR
        1: 5,  # TFL -> BFL
        2: 6,  # TBL -> BBL
        3: 7   # TBR -> BBR
    }
    
    # If the piece is already in the top layer above its target position, no alignment needed
    if current_position in top_to_bottom and top_to_bottom[current_position] == target_position:
        return []
    
    # Determine how many U moves needed to align
    if current_position not in [0, 1, 2, 3]:
        # This shouldn't happen if we've moved the piece to the top layer
        return ["U"]  # Default to one U move if something went wrong
    
    # Calculate required U moves for alignment
    if target_position == 4:  # BFR
        required_position = 0  # TFR
    elif target_position == 5:  # BFL
        required_position = 1  # TFL
    elif target_position == 6:  # BBL
        required_position = 2  # TBL
    elif target_position == 7:  # BBR
        required_position = 3  # TBR
    
    # Calculate the number of U moves needed
    diff = (required_position - current_position) % 4
    
    if diff == 0:
        return []
    elif diff == 1:
        return ["U"]
    elif diff == 2:
        return ["U2"]
    else:  # diff == 3
        return ["U'"]

def get_insertion_moves(target_position, orientation):
    """
    Get the sequence of moves to insert a corner into its target position with correct orientation
    """
    # Different insertion algorithms based on the target position and current orientation
    if target_position == 4:  # BFR
        if orientation == 0:
            return ["R", "U2", "R'", "U'", "R", "U", "R'"]
        elif orientation == 1:
            return ["R", "U", "R'"]
        else:  # orientation == 2
            return ["F'", "U'", "F"]
    
    elif target_position == 5:  # BFL
        if orientation == 0:
            return ["F", "U2", "F'", "U'", "F", "U", "F'"]
        elif orientation == 1:
            return ["F", "U", "F'"]
        else:  # orientation == 2
            return ["L'", "U'", "L"]
    
    elif target_position == 6:  # BBL
        if orientation == 0:
            return ["L", "U2", "L'", "U'", "L", "U", "L'"]
        elif orientation == 1:
            return ["L", "U", "L'"]
        else:  # orientation == 2
            return ["B'", "U'", "B"]
    
    elif target_position == 7:  # BBR
        if orientation == 0:
            return ["B", "U2", "B'", "U'", "B", "U", "B'"]
        elif orientation == 1:
            return ["B", "U", "B'"]
        else:  # orientation == 2
            return ["R'", "U'", "R"]
    
    return []  # Default empty list if no match

# Test function
def test_first_layer_solver():
    from cube import Cube  # Import your Cube class
    
    # Create a new cube and scramble it
    cube = Cube()
    print("Initial state (solved):")
    print(cube)
    
    # Apply a scramble
    scramble = ["R", "U", "F","U'", "R'"]
    apply_and_print(cube,scramble)
    print("\nScrambled state:")
    print(cube)
    
    # Solve the first layer
    print("\nSolving first layer...")
    solve_first_layer(cube)
    
    # Check if bottom corners are solved
    bottom_corners_solved = all(
        cube.positions[i] == i and cube.orientations[i] == 0
        for i in [4, 5, 6, 7]
    )
    
    print("\nFinal state:")
    print(cube)
    print(f"\nBottom layer corners solved: {bottom_corners_solved}")

