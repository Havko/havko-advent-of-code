def load_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
input_text = load_input('day2_input.txt')

def evaluate_report(report):
    print(report)

for line in input_text.split('\n'):
    report = line.split()