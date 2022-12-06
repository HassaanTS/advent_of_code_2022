test_file = 'test_files/test06.txt';
# test_file = 'test_files/test_file.txt';

data = open(test_file,'r').read()

def part1():
    left = 0;
    right = left + 4;
    while left <= len(data):
        # print(data[left:right])
        if len(list(set(data[left:right]))) == 4:
            return right
        else:
            left += 1
            right = left + 4
# print(part1())

def part2():
    left = 0;
    right = left + 14;
    while left <= len(data):
        if len(list(set(data[left:right]))) == 14:
            return right
        else:
            left += 1
            right = left + 14
print(part2())