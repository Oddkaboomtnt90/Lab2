import statistics
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)
    calc_median_temperature(num_list)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)")


def get_user_input():
    Inputs = input()
    FloatList = list(map(float, Inputs.split(",")))
    return FloatList


def calc_average_temperature(ListOfNumber):
    sum = 0
    for x in ListOfNumber:
        sum += x
    average = sum/len(ListOfNumber)
    print("Average = " + str(average))
    return average

def calc_min_max_temperature(ListOfNumber):
    Minimum = min(ListOfNumber)
    Maximum = max(ListOfNumber)
    print("Maximum = " + str(Maximum))
    print("Minimum = " + str(Minimum))
    return Maximum,Minimum

def calc_median_temperature(ListOfNumber):
    Median = statistics.median(ListOfNumber)
    print("Median = ", Median)
    return Median

if __name__ == "__main__":
    main()
