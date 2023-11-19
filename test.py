def mass_conversion():
    standard_conversions_available = [(1, 'oz', 'mg'),
                                      (2, 'oz', 'g'),
                                      (3, 'lb', 'g'),
                                      (4, 'lb', 'kg'),
                                      (5, 'stone', 'kg'),
                                      (6, 'US ton', 'kg/t'),
                                      (7, 'Imperial ton', 'kg/t')]

    metric_conversions_available = [(1, 'mg', 'oz'),
                                    (2, 'g', 'oz'),
                                    (3, 'kg', 'oz'),
                                    (4, 'kg', 'lb'),
                                    (5, 'kg', 'US/Imperial ton'),
                                    (6, 'Ton', 'US/Imperial ton')]
    while True:
        print()
        print("1 for metrics to standard. 2 for standard to metrics. ")
        len_choice = int(input("Please input your choice of conversion: "))
        if len_choice in (1, 2):
            break
        else:
            print('Invalid Input. ')

    if len_choice == 2:

        print()
        print("STANDARD CONVERSIONS AVAILABLE: ")
        print()

        for conversion_number, input_unit, output_unit in standard_conversions_available:
            print(str(conversion_number) + ". " + str(input_unit) + " --> " + str(output_unit))
        print()
        while True:
            conversion_index = int(input("Enter conversion number: ")) - 1
            if conversion_index in (0, 1, 2, 3, 4, 5, 6):
                break
            else:
                print("Invalid input. Only enter numbers 1-7")

        print()
        in_val = float(input("Enter input unit: "))
        print()

        if conversion_index == 0:
            out_val = str(in_val * 28350)
            print(str(in_val) + " in ounces is " + out_val + " in mg")

        if conversion_index == 1:
            out_val = str(in_val * 28.35)
            print(str(in_val) + " in ounces is " + out_val + " in g")

        if conversion_index == 2:
            out_val = str(in_val * 453.6)
            print(str(in_val) + " in lb is " + out_val + " in g")

        if conversion_index == 3:
            out_val = str(in_val / 2.205)
            print(str(in_val) + " in lb is " + out_val + " in kg")

        if conversion_index == 4:
            out_val = str(in_val * 6.35)
            print(str(in_val) + " in stones is " + out_val + " in kg")

        if conversion_index == 5:
            out_val1 = str(in_val * 907.2)
            out_val2 = str(in_val / 1.102)
            print(str(in_val) + " in US tonnes is " + out_val1 + " in kg and " + out_val2 + " in tonnes")

        if conversion_index == 6:
            out_val1 = str(in_val * 1016)
            out_val2 = str(in_val * 1.016)
            print(str(in_val) + " in Imperial tonnes is " + out_val1 + " in kg and " + out_val2 + " in tonnes")

    if len_choice == 1:

        print()
        print("METRIC CONVERSIONS AVAILABLE: ")
        print()

        for conversion_number, input_unit, output_unit in metric_conversions_available:
            print(str(conversion_number) + ". " + str(input_unit) + " --> " + str(output_unit))
        print()
        while True:
            conversion_index = int(input("Enter conversion number: ")) - 1
            if conversion_index in (0, 1, 2, 3, 4, 5):
                break
            else:
                print("Invalid input. Only enter numbers 1-8")

        print()
        in_val = float(input("Enter input unit: "))
        print()

        if conversion_index == 0:
            out_val = str(in_val/28350)
            print(str(in_val) + " in mg is " + out_val + " in ounces")

        if conversion_index == 1:
            out_val = str(in_val/28.35)
            print(str(in_val) + " in g is " + out_val + " in ounces")

        if conversion_index == 2:
            out_val = str(in_val * 35.274)
            print(str(in_val) + " in kg is " + out_val + " in ounces")

        if conversion_index == 3:
            out_val = str(in_val * 2.205)
            print(str(in_val) + " in kg is " + out_val + " in lb")

        if conversion_index == 5:
            out_val1 = str(in_val / 907.2)
            out_val2 = str(in_val / 1016)
            print(str(in_val) + " in kg is " + out_val1 + " in US tonnes and " + out_val2 + " in Imperial tonnes")

        if conversion_index == 6:
            out_val1 = str(in_val * 1.102)
            out_val2 = str(in_val / 1.016)
            print(str(in_val) + " in tonnes is " + out_val1 + " in US tonnes and " + out_val2 + " in Imperial tonnes")
