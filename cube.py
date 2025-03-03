class Cube:
    def __init__(self):
        self.positions = list(range(8))
        self.orientations = [0] * 8
    
    def get_state(self):
        corner_names = ["TFR", "TFL", "TBL", "TBR", "BFR", "BFL", "BBL", "BBR"]
        state = []
        for pos in range(8):
            piece_idx = self.positions.index(pos)
            orientation = self.orientations[piece_idx]
            state.append(f"Position {corner_names[pos]}: Piece {piece_idx} with orientation {orientation}")
        return "\n".join(state)

    def apply_move(self, moves):
        if isinstance(moves, str):
            moves = [moves]
        for move in moves:
            if move == 'R':
                self._rotate_face(cycle=[0, 3, 7, 4], delta=1)
            elif move == "R'":
                self._rotate_face(cycle=[0, 3, 7, 4], delta=1)
                self._rotate_face(cycle=[0, 3, 7, 4], delta=1)
                self._rotate_face(cycle=[0, 3, 7, 4], delta=1)
            elif move == 'R2':
                self._rotate_face(cycle=[0, 3, 7, 4], delta=1)
                self._rotate_face(cycle=[0, 3, 7, 4], delta=1)
            elif move == 'L':
                self._rotate_face(cycle=[1, 5, 6, 2], delta=1)
            elif move == "L'":
                self._rotate_face(cycle=[1, 5, 6, 2], delta=1)
                self._rotate_face(cycle=[1, 5, 6, 2], delta=1)
                self._rotate_face(cycle=[1, 5, 6, 2], delta=1)
            elif move == 'L2':
                self._rotate_face(cycle=[1, 5, 6, 2], delta=1)
                self._rotate_face(cycle=[1, 5, 6, 2], delta=1)
            elif move == 'U':
                self._rotate_face(cycle=[0, 1, 2, 3], delta=0)
            elif move == "U'":
                self._rotate_face(cycle=[0, 1, 2, 3], delta=0)
                self._rotate_face(cycle=[0, 1, 2, 3], delta=0)
                self._rotate_face(cycle=[0, 1, 2, 3], delta=0)
            elif move == 'U2':
                self._rotate_face(cycle=[0, 1, 2, 3], delta=0)
                self._rotate_face(cycle=[0, 1, 2, 3], delta=0)
            elif move == 'D':
                self._rotate_face(cycle=[4, 7, 6, 5], delta=0)
            elif move == "D'":
                self._rotate_face(cycle=[4, 7, 6, 5], delta=0)
                self._rotate_face(cycle=[4, 7, 6, 5], delta=0)
                self._rotate_face(cycle=[4, 7, 6, 5], delta=0)
            elif move == 'D2':
                self._rotate_face(cycle=[4, 7, 6, 5], delta=0)
                self._rotate_face(cycle=[4, 7, 6, 5], delta=0)
            elif move == 'F':
                self._rotate_face(cycle=[0, 4, 5, 1], delta=2)
            elif move == "F'":
                self._rotate_face(cycle=[0, 4, 5, 1], delta=2)
                self._rotate_face(cycle=[0, 4, 5, 1], delta=2)
                self._rotate_face(cycle=[0, 4, 5, 1], delta=2)
            elif move == 'F2':
                self._rotate_face(cycle=[0, 4, 5, 1], delta=2)
                self._rotate_face(cycle=[0, 4, 5, 1], delta=2)
            elif move == 'B':
                self._rotate_face(cycle=[3, 2, 6, 7], delta=2)
            elif move == "B'":
                self._rotate_face(cycle=[3, 2, 6, 7], delta=2)
                self._rotate_face(cycle=[3, 2, 6, 7], delta=2)
                self._rotate_face(cycle=[3, 2, 6, 7], delta=2)
            elif move == 'B2':
                self._rotate_face(cycle=[3, 2, 6, 7], delta=2)
                self._rotate_face(cycle=[3, 2, 6, 7], delta=2)
    
    def _rotate_face(self, cycle, delta):
        # Collect physical pieces in the cycle
        physical_pieces = [self.positions.index(pos) for pos in cycle]
        
        # Update positions
        new_positions = self.positions.copy()
        for i in range(4):
            new_positions[physical_pieces[i]] = cycle[(i + 1) % 4]
        self.positions = new_positions
        
        # Update orientations
        if delta != 0:
            for i, phys_piece in enumerate(physical_pieces):
                old_pos = cycle[i]
                new_pos = cycle[(i + 1) % 4]
                
                # If moving between top/bottom layers, adjust orientation
                if (old_pos < 4 and new_pos >= 4) or (old_pos >= 4 and new_pos < 4):
                    self.orientations[phys_piece] = (self.orientations[phys_piece] + 2) % 3
                else:
                    self.orientations[phys_piece] = (self.orientations[phys_piece] + 1) % 3

    def is_solved(self):
        if self.positions != list(range(8)):
            return False
        if any(self.orientations):
            return False
        return True
    
    def __str__(self):
        return self.get_state()

