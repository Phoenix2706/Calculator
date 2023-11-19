def main_menu():
    choice = int(input('1. Length\n'
                       '2. Mass\n'
                       '3. Quit\n'
                       'Enter your choice: '))
    return choice


def get_conversion_menu(measurement_type):
    if measurement_type == 'standard':
        conversions = ['1. Ounces(oz) to Milliliters(ml)', '2. Ounces(oz) to Liters(L)',
                       '3. Cups to Milliliters(ml)', '4. Cups to Liters(L)',
                       '5. Pints(pt) to Milliliters(ml)', '6. Pints(pt) to Liters(L)',
                       '7. Gallons(gal) to Liters(L)']
    elif measurement_type == 'metric':
        conversions = ['1. Milliliters(ml) to Ounces(oz)', '2. Liters(L) to Ounces(oz)',
                       '3. Milliliters(ml) to Cups', '4. Liters(L) to Cups',
                       '5. Milliliters(ml) to Pints(pt)', '6. Liters(L) to Pints(pt)',
                       '7. Liters(L) to Gallons(gal)']
        for every_con in conversions:
            print(conversion)
    choice = int(input('Enter your choice: '))
    return choice


def conversion(measurement_type, conversion_index, in_val):
    if measurement_type == 'standard':
        conversion_formulas = [in_val * 29.5735, in_val * 0.0295735, in_val * 237.588, in_val * 0.237588,
                               in_val * 473.176,
                               in_val * 0.473176, in_val * 3.78541]
        units = ['ml', 'L', 'ml', 'L', 'ml', 'L', 'L']
    elif measurement_type == 'metric':
        conversion_formulas = [in_val * 0.033814, in_val * 33.814, in_val * 0.00422675, in_val * 4.22675,
                               in_val * 0.00211338,
                               in_val * 2.11338, in_val * 0.264172]
        units = ['oz', 'oz', 'cups', 'cups', 'pt', 'pt', 'gal']

    result = conversion_formulas[conversion_index - 1]
    print(f'{in_val} {units[conversion_index - 1]} is {result}')


choice = main_menu()
while choice != 3:
    if choice == 1:
        conversion_index = get_conversion_menu('standard')
        in_val = float(input('Enter your volume: '))
        conversion('standard', conversion_index, in_val)
    elif choice == 2:
        conversion_index = get_conversion_menu('metric')
        in_val = float(input('Enter your volume: '))
        conversion('metric', conversion_index, in_val)
    else:
        print('Invalid choice.')
    choice = main_menu()