import random

def player(prev_play, opponent_history=[]):
    # Track opponent's history
    if prev_play:
        opponent_history.append(prev_play)

    # Default move for the first round
    if not opponent_history:
        return random.choice(["R", "P", "S"])

    # Strategy: Predict the most frequent move and counter it
    most_common = max(set(opponent_history), key=opponent_history.count)
    
    # Counter the most common move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    
    return counter_moves[most_common]
