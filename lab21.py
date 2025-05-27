def display_main_menu():
    print("display_main_menu")

def get_user_input():
    print("get_user_input")
    user_input =input()
    str_list = user_input.split(",")
    return [float(num.strip()) for num in str_list]

def calc_average(lst):
    print("calc_average")
    return sum(lst) / len(lst)

def find_min_max(lst):
    print("find_min_max")
    return [min(lst), max(lst)]

def sort_temperature(lst):
    print("sort_temperature")
    return sorted(lst)

def calc_median_temperature(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
    
def main():
    display_main_menu()
    num_list = get_user_input()
    print("Average =", calc_average(num_list))
    print("Min/Max =", find_min_max(num_list))
    print("Sorted =", sort_temperature(num_list))
    print("Median =", calc_median_temperature(num_list))

if __name__ == "__main__":
    main()
