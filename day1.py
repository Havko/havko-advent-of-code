def load_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def calculate_dif(item1, item2):
    print("Comparing:")
    print(item1, item2)
    print(abs(int(item1) - int(item2)))
    return abs(int(item1) - int(item2))

input_text = load_input('day1_input.txt')

list1 = []
list2 = []
diffScore = 0
for line in input_text.split('\n'):
    split_line = line.split()
    list1.append(split_line[0])
    list2.append(split_line[1])
list1.sort()
list2.sort()
for i in range(0, len(list1)):
    diffScore += calculate_dif(list1[i], list2[i])

print(diffScore)
