import sys

if __name__ == "__main__":

    # user inputs
    def first_method():

        portion_down_payment = .25
        current_savings = 0
        r = .04
        month = 0

        total_cost = float(input("Enter Total Cost: "))
        annual_salary = float(input("Enter your annual salary: "))
        portion_saved  = float(input("Enter the percent of your salary to save: "))
        semi_annual_raise = float(input("Enter the raise percent: "))
        # main loop

        while (current_savings < total_cost * portion_down_payment):
            current_savings += current_savings * r / 12 + annual_salary / 12 * portion_saved
            month += 1
            if month % 6 == 0:
                annual_salary += annual_salary * semi_annual_raise
        return month


# Problem C

annual_salary = float(input("What is your annual salary: "))
total_cost = 1000000
portion_down_payment = .25
savings_needed = portion_down_payment * total_cost
nums = [num / 10000 for num in range(1,10000)]

def binary_search(search_list):
    if helper(1)  < savings_needed:
        sys.exit("It is not possible to pay the down payment in three years.")
    iterations = 1
    left = 0
    right = len(search_list) - 1
    mid = (right + left) // 2
    while True:
        value = helper(search_list[mid])
        if value < savings_needed - 100 or value > savings_needed + 100:
            if  value < savings_needed - 100:
                left = mid + 1
            else:
                right = mid - 1
        else:
            break
        mid = (right + left) // 2
        iterations += 1
    print(mid / 10000)
    print(iterations)

def helper(portion_saved):
    current_savings = 0
    r = .04
    month = 0
    total_month = 36
    salary = annual_salary
    portion_saved = portion_saved
    semi_annual_raise = .07
    # main loop

    while (month < total_month):
        current_savings += current_savings * r / 12 + salary / 12 * portion_saved
        month += 1
        if month % 6 == 0:
            salary += salary * semi_annual_raise
    return current_savings

binary_search(nums)

