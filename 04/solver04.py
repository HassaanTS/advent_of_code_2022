test_file = 'test_files/test04.txt';
# test_file = 'test_files/test_file.txt';

data = open(test_file,'r').read().splitlines()

def conv_int(_str):
    _str = _str.split('-')
    return int(_str[0]) , int(_str[1])
def is_between(_target, left_range, right_range):
    return left_range <= _target and _target <= right_range

def part1():
    overlap = 0;
    for elem in data:
        left, right = elem.split(',')
        l1, l2 = conv_int(left)
        r1, r2 = conv_int(right)
        if (is_between(l1, r1, r2) and is_between(l2, r1, r2)) or (is_between(r1, l1, l2) and is_between(r2, l1, l2)):
            # print(f"left: {left} | right: {right}")
            overlap+=1
    return overlap
# print(part1())


def part2():
    overlap = 0
    for elem in data:
        left, right = elem.split(',')
        l1, l2 = conv_int(left)
        r1, r2 = conv_int(right)
        if is_between(l1, r1, r2) or is_between(l2, r1, r2) or is_between(r1, l1, l2) or is_between(r2, l1, l2):
            # print(f"left: {left} | right: {right}")
            overlap+=1
    return overlap
print(part2())