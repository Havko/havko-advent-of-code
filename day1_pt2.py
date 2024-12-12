def load_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def search_list(input_list, target):
    count = 0
    for i in range(0, len(input_list)):
        if input_list[i] == target:
            count += int(target)
    return count

diff_score = 0
input_text = load_input('day1_input.txt')

list1 = []
list2 = []
diffScore = 0
for line in input_text.split('\n'):
    split_line = line.split()
    list1.append(split_line[0])
    list2.append(split_line[1])

for item in list1:
    diffScore += search_list(list2, item)

print(diffScore)