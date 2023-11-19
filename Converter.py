def check_integer(input_result):
    if isinstance(input_result, float):
        if input_result.is_integer():
            input_result = int(input_result)
    return input_result


def main_menu():
    while True:
        try:
            con_type = int(input('1. Mass\n'
                                 '2. Length\n'
                                 '3. Quit\n'
                                 'Enter your type of conversion: '))
            print()
        except ValueError:
            print("Invalid input. Only enter a number ")
        else:
            break

    while True:
        try:
            con_way = int(input('1. Standard to Metric conversion\n'
                                '2. Metric to standard conversion\n'
                                'Enter your unit of conversion: '))
            print()
        except ValueError:
            print("Invalid input. Only enter a number ")
        else:
            break

    return [con_type, con_way]


def input_conversion_choice(con_type, con_way):

    while True:
        try:
            in_val = float(input("Enter input value: "))
            print()
        except ValueError:
            print("Invalid input. Only enter a number ")
        else:
            break

    if con_type == 1 and con_way == 1:  # standard to metric mass conversion
        con_available = [(1, 'oz', 'mg'),
                         (2, 'oz', 'g'),
                         (3, 'oz', 'kg'),
                         (4, 'lb', 'g'),
                         (5, 'lb', 'kg'),
                         (6, 'US ton', 'kg'),
                         (7, 'US ton', 'ton'),
                         (8, 'Imperial ton', 'kg'),
                         (9, 'Imperial ton', 'ton')]

        con_formulas = [in_val * 28350, in_val * 28.35, in_val / 35.274, in_val * 453.6, in_val / 2.205,
                        in_val * 907.2, in_val / 1.102, in_val * 1016, in_val * 1.016]

    elif con_type == 1 and con_way == 2:  # metric to standard mass conversion

        con_available = [(1, 'mg', 'oz'),
                         (2, 'g', 'oz'),
                         (3, 'g', 'lb'),
                         (4, 'kg', 'oz'),
                         (5, 'kg', 'lb'),
                         (6, 'kg', 'US ton'),
                         (7, 'kg', 'Imperial ton'),
                         (8, 'Ton', 'US ton'),
                         (9, 'Ton', 'Imperial ton')]

        con_formulas = [in_val / 28350, in_val / 28.35, in_val / 453.6, in_val * 35.274, in_val * 2.205,
                        in_val / 907.2, in_val / 1016, in_val * 1.102, in_val / 1.016]

    elif con_type == 2 and con_way == 1:  # standard to metric length conversion

        con_available = [(1, 'in', 'mm'),
                         (2, 'in', 'cm'),
                         (3, 'ft', 'mm'),
                         (4, 'ft', 'cm'),
                         (5, 'ft', 'm'),
                         (6, 'yd', 'm'),
                         (7, 'yd', 'km'),
                         (8, 'mi', 'km')]

        con_formulas = [in_val * 25.4, in_val * 2.54, in_val * 304.8, in_val * 30.48, in_val / 3.281,
                        in_val / 1.094, in_val / 1094, in_val * 1.609]

    elif con_type == 2 and con_way == 2:  # metric to standard length conversion

        con_available = [(1, 'mm', 'in'),
                         (2, 'mm', 'ft'),
                         (3, 'cm', 'in'),
                         (4, 'cm', 'ft'),
                         (5, 'm', 'ft'),
                         (6, 'm', 'yd'),
                         (7, 'km', 'yd'),
                         (8, 'km', 'mi')]

        con_formulas = [in_val / 25.4, in_val / 304.8, in_val / 2.54, in_val / 30.48, in_val / 3.281,
                        in_val * 1.094, in_val * 1094, in_val / 1.609]

    print("AVAILABLE CONVERSIONS: ")
    for con_number, input_unit, output_unit in con_available:
        print(str(con_number) + ". " + str(input_unit) + " --> " + str(output_unit))

    while True:
        con_index = int(input("Enter conversion number: ")) - 1
        if con_index in range(len(con_available)):
            break
        else:
            print("Invalid input. Only enter numbers 1-" + str(len(con_available)))

    result = con_formulas[con_index]

    result = check_integer(result)
    in_val = check_integer(in_val)

    input_unit, output_unit = con_available[con_index][1:]
    print()
    print(f"{in_val}{input_unit} is {result}{output_unit}")


con_info_1, con_info_2 = main_menu()

input_conversion_choice(con_info_1, con_info_2)
