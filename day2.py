def load_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
input_text = load_input('day2_input.txt')

def is_incrementing(val1, val2):
    if int(val1) < int(val2):
        return True
    return False

def is_decrementing(val1, val2):
    if int(val1) > int(val2):
        return True
    return False


def evaluate_report(report):
    is_safe = True
    is_incrementing_bool = is_incrementing(report[0], report[1])
    is_decrementing_bool = is_decrementing(report[0], report[1])
    if(report[0] == report[1]):
        return False
    
    for i in range(1, len(report)):
        val1 = int(report[i - 1])
        val2 = int(report[i])
        if(val1 == val2):
            is_safe = False
            break      
        if(abs(val1 - val2) > 3):
            is_safe = False
            break
        if(is_incrementing_bool):
            if(not is_incrementing(val1, val2)):
                is_safe = False
                break
        if(is_decrementing_bool):
            if(not is_decrementing(val1, val2)):
                is_safe = False
                break
    if(is_safe):
        print(report)
    return is_safe
        
        
        
        
count = 0
for line in input_text.split('\n'):
    report = line.split()
    if(evaluate_report(report)):
        count += 1
print(count)