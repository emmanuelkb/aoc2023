# First Question
def calibration_values_sum(file_name):
    total_sum = 0

    with open(file_name, "r") as file:
        for line in file:
            numbers = [current for current in line if current.isdigit()]
            line_combined = numbers[0] + numbers[-1]
            total_sum += int(line_combined)
            print("total:", total_sum)
        return total_sum


# Second Question

def convert_text_to_number(file_name):
    total_sum = 0
    conversion = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }
    with open(file_name, "r") as file:
        for line in file:
            print("initial word: ", line)
            for key in conversion.keys():
                res = line.find(key)
                if res >= 0:
                    line = line.replace(key, conversion[key])
            print("converted word: ", line)
            numbers = [current for current in line if current.isdigit()]
            print(numbers)
            line_combined = numbers[0] + numbers[-1]
            print(line_combined)
            total_sum += int(line_combined)
            print("total:", total_sum)
    return total_sum


if __name__ == "__main__":
    print(convert_text_to_number("day1/input.txt"))
