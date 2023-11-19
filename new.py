def main_menu():
    con_type = int(input('1. Length\n'
                         '2. Mass\n'
                         '3. Quit\n'
                         'Enter your choice: '))

    con_way = int(input('1. Metric to standard\n'
                        '2. Standard to metric\n'))
    return [con_type, con_way]


def input_conversion_choice(measurement_type, con_way):
    measurement_type = int(measurement_type)
    con_way = int(con_way)

    while True:
        try:
            in_val = float(input("Enter input unit: "))
        except ValueError:
            print("Invalid input. Only enter a number ")
        else:
            break

    if measurement_type == 1 and con_way == 1:  # mass conversion from metric to standard
        conversions_available = [(1, 'oz', 'mg'),
                                 (2, 'oz', 'g'),
                                 (3, 'lb', 'g'),
                                 (4, 'lb', 'kg'),
                                 (5, 'stone', 'kg'),
                                 (6, 'US ton', 'kg'),
                                 (7, 'US ton', 'ton'),
                                 (8, 'Imperial ton', 'kg'),
                                 (9, 'Imperial ton', 'ton')]
        conversion_formulas = [in_val * 28350, in_val * 28.35, in_val * 453.6, in_val / 2.205, in_val * 6.35
            , in_val * 907.2, in_val / 1.102, in_val * 1016, in_val * 1.016]

    elif measurement_type == 1 and con_way == 2:  # mass conversion from standard to metric
        conversions_available = [(1, 'mg', 'oz'),
                                 (2, 'g', 'oz'),
                                 (3, 'kg', 'oz'),
                                 (4, 'kg', 'lb'),
                                 (5, 'kg', 'US/Imperial ton'),
                                 (6, 'Ton', 'US/Imperial ton')]
        conversion_formulas = [in_val / 28350, in_val / 28.35, in_val / 453.6, in_val * 2.205, in_val / 6.35
            , in_val / 907.2, in_val * 1.102, in_val / 1016, in_val / 1.016]

    for conversion_number, input_unit, output_unit in conversions_available:
        print(str(conversion_number) + ". " + str(input_unit) + " --> " + str(output_unit))

    while True:
        conversion_index = int(input("Enter conversion number: ")) - 1
        if conversion_index in range(len(conversions_available)):
            break
        else:
            print(f"Invalid input. Only enter numbers 1-{len(conversions_available)}")

    result = conversion_formulas[conversion_index]
    input_unit, output_unit = conversions_available[conversion_index][1:]
    print(f"{in_val} {input_unit} is {result} {output_unit}")


coninfo1, coninfo2 = main_menu()

input_conversion_choice(coninfo1, coninfo2)
