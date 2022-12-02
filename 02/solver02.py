test_file = 'test_files/test02.txt';
# test_file = 'test_files/test_file.txt';

data = open(test_file,'r').read().splitlines()


game_result_dict = {
    'W': 6,
    'D': 3,
    'L': 0
}

strategy_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

game_result = {
    'A X': 'D',
    'A Y': 'W',
    'A Z': 'L',
    'B X': 'L',
    'B Y': 'D',
    'B Z': 'W',
    'C X': 'W',
    'C Y': 'L',
    'C Z': 'D',
}

def part1(): # return score
    score = 0;
    for elem in data:
        # add game result points
        score += game_result_dict[game_result[elem]]

        #add points for strategy
        score += strategy_points[elem.split(' ')[1]]
    return score
# print(part1())


new_game_result_dict = {
    'Z': 6,
    'Y': 3,
    'X': 0
}

new_strategy_points = {
    'A': 1,
    'B': 2,
    'C': 3
}

new_strategy_choice = {
    'A X': 'C',
    'A Y': 'A',
    'A Z': 'B',
    'B X': 'A',
    'B Y': 'B',
    'B Z': 'C',
    'C X': 'B',
    'C Y': 'C',
    'C Z': 'A',
}

def part2(): # return score
    score = 0;
    for elem in data:
        # add points for strategy
        score += new_strategy_points[new_strategy_choice[elem]]

        #add points for game outcome
        score += new_game_result_dict[elem.split(' ')[1]]
    return score
print(part2())