import re
test_file = 'test_files/test05.txt';
# test_file = 'test_files/test_file_instructions.txt';

f = open(test_file);
data = open(test_file,'r').read().splitlines()

small_dict = {
    1: ['Z', 'N'],
    2: ['M', 'C', 'D'],
    3: ['P'],
}

big_dict = {
    1: ['F', 'D','B','Z','T','J','R','N'],
    2: ['R','S','N','J','H'],
    3: ['C','R','N','J','G','Z','F','Q'],
    4: ['F','V','N','G','R','T','Q'],
    5: ['L','T','Q','F'],
    6: ['Q','C','W','Z','B','R','G','N'],
    7: ['F','C','L','S','N','H','M'],
    8: ['D','N','Q','M','T','J'],
    9: ['P','G','S'],
}

def part1():
    _dict = big_dict
    message = ''
    for elem in data:
        _moves, _from, _to = re.findall(r'\d+',elem)
        _moves, _from, _to = int(_moves), int(_from), int(_to)
        for i in range(_moves):
            buff = _dict[_from].pop()
            _dict[_to].append(buff)
    for key in _dict:
        message+=_dict[key].pop()
    return message

print(part1())

def part2():
    _dict = big_dict
    buff = []
    message = ''
    for elem in data:
        _moves, _from, _to = re.findall(r'\d+',elem)
        _moves, _from, _to = int(_moves), int(_from), int(_to)
        for i in range(_moves):
            buff.append(_dict[_from].pop())
        _dict[_to]+=(buff[::-1])
        buff = []
    for key in _dict:
        message+=_dict[key].pop()
    return message

print(part2())