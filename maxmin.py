
user_number = input("Enter your list of numbers separated by commas:  ").replace(
    "[", "").replace("]", "")
number_list = [int(user_number.split(",")[i])
               for i in range(len(user_number.split(",")))]


def min_max_calculator(input_list):
    min_max = None

    for i in range(len(input_list)):
        if i == 0:
            min_max = [input_list[i], input_list[i]]
        else:
            # checking for min or max values
            if input_list[i] < min_max[0]:
                min_max[0] = input_list[i]
            elif number_list[i] > min_max[1]:
                min_max[1] = input_list[i]

    return min_max


print(min_max_calculator(number_list))
