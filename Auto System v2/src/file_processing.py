def process_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        numbers = []
        for line in lines:
            for item in line.split():
                if item.isdigit():
                    numbers.append(int(item))
        numbers.sort()
        numbers.append(9999)
        with open(output_file, 'w') as file:
            for num in numbers:
                file.write(f"{num}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
