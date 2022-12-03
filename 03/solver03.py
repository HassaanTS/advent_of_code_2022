# test_file = 'test_files/test03.txt';
test_file = 'test_files/test_file.txt';

data = open(test_file,'r').read().splitlines()

list_lower = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26
    }


def part1(): 
    score = 0;
    for elem in data:
        half_mark = len(elem)/2
        first_compartment = set(elem[:half_mark])
        second_compartment = set(elem[half_mark:])
        common_elem = (first_compartment&second_compartment).pop()
        score += (ord(common_elem)-96) if common_elem.islower() else (ord(common_elem.lower())-96+26)
        # if common_elem in list_lower:
        #     score+=list_lower[common_elem]
        # else: 
        #     score+=list_lower[common_elem.lower()]+26
    return score
print(part1())


def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return zip(*[iter(iterable)]*n)
def part2(): 
    score = 0;
    for x, y, z in grouped(data, 3):
        common_elem = (set(x) & set(y) & set(z)).pop()
        score += (ord(common_elem)-96) if common_elem.islower() else (ord(common_elem.lower())-96+26)
        # if common_elem in list_lower:
        #     score+=list_lower[common_elem]
        # else: 
        #     score+=list_lower[common_elem.lower()]+26
    return score
print(part2())