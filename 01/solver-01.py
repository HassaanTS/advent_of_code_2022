
test_file = 'test_files/test01.txt';
# test_file = 'test_files/test_file.txt';

f = open(test_file);
data = f.readlines();


def part1(): # return top
    adding_list = [];
    most_calories = [];
    for i in range(len(data)):
        if(len(data[i].strip()) == 0): #empty line: reset list
            most_calories.append(sum(adding_list));
            adding_list = [];
        else:
            adding_list.append(int(data[i]));
    if adding_list != []:
        most_calories += adding_list
    return sorted(most_calories, reverse=True)[0];
print(part1())

def part2(): # return top 3
    adding_list = [];
    most_calories = [];
    for i in range(len(data)):
        if(len(data[i].strip()) == 0): #empty line: reset list
            most_calories.append(sum(adding_list));
            adding_list = [];
        else:
            adding_list.append(int(data[i]));
    if adding_list != []:
        most_calories += adding_list
    return sum(sorted(most_calories, reverse=True)[0:3]);
# print(part2())