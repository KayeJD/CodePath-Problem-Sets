def calculate_expenses(expenses):
    # print('yip')

    # Initialize dict with the expenses
    dict_expense = {}
    most_expensive = 0
    output = ""

    # access each tuple
    # access each category
        # if category is not in dict
            # add the category to the dict
            # add the expense to dict[category]

        # compare the current category[expense] to most_expensive
            # if category[expense] > most_expensive
    
    for expense in expenses:
        # print(expense[0], expense[1])
        if expense[0] not in dict_expense:
            dict_expense[expense[0]] = 0

        dict_expense[expense[0]] += expense[1]
        
        if dict_expense[expense[0]] > most_expensive:
            output = expense[0]

    return (expenses, output)



expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))

"""
({'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')
({'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}, 'Food')
({'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}, 'Utilities')
"""