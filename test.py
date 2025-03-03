from cube import Cube
from rubiks_cube_first_layer_solver import solve_first_layer
from rubiks_cube_second_layer_solver import solve_second_layer


def main():
    scramble = input("Enter scramble sequence: ").split()
    cube = Cube()
    
    # Apply scramble
    cube.apply_move(scramble)
    print("Scrambled cube:")
    print(cube)
    
    # Solve first layer
    solve_first_layer(cube)
    # Solve second layer
    solve_second_layer(cube)

    
    # Verify if solved
    if cube.is_solved():
        print("Cube is solved!")
    else:
        print("Solution failed.")

if __name__ == "__main__":
    main()
