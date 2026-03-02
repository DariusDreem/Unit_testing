def calculate_strikes(score, rolls, roll_index):
    score += 10
    if roll_index + 1 < len(rolls):
        score += rolls[roll_index + 1]
    if roll_index + 2 < len(rolls):
        score += rolls[roll_index + 2]
    roll_index += 1
    return score,roll_index
    
def calculate_spares(score, rolls, roll_index):
    score += 10
    if roll_index + 2 < len(rolls):
        score += rolls[roll_index + 2]
    roll_index += 2
    return score,roll_index
    
def calculate_open_frames(score, rolls, roll_index):
    score += rolls[roll_index] + rolls[roll_index + 1]
    roll_index += 2
    return score,roll_index

def calculate_score(rolls):
    score = 0
    roll_index = 0
    
    for frame in range(10):
        if roll_index >= len(rolls):
            break
            
        if rolls[roll_index] == 10:  # Strike
            score, roll_index = calculate_strikes(score, rolls, roll_index)
            
        elif roll_index + 1 < len(rolls) and rolls[roll_index] + rolls[roll_index + 1] == 10:  # Spare
            score, roll_index = calculate_spares(score, rolls, roll_index)
            
        else:  # Open frame
            score, roll_index = calculate_open_frames(score, rolls, roll_index)
    
    return score