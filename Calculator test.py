import math
from math import pi

print("***************************************************")
print("************WELCOME TO MY CALCULATOR************")
print("***************************************************")
print()


def check_integer(input_result):
    if isinstance(input_result, float):
        if input_result.is_integer():
            input_result = int(input_result)
    return input_result


def collect_inputs():
    inputs = []
    count = 1
    order = "st"
    while True:
        if count == 2:
            order = "nd"
        elif count == 3:
            order = "rd"
        elif count >= 4:
            order = "th"
        val = input("Enter the " + str(count) + order + " number (or (Q)uit): ")
        print()
        if val.upper() == 'Q':
            break
        elif val.isdigit():
            inputs.append(int(val))
            count += 1
        else:
            print("Invalid input. Please enter a number. ")
            print()
    return inputs


def calculate_trigonometric_values():
    angle_degrees = float(input("Input angles in degrees: "))
    print()
    # Convert angle from degrees to radians
    rad_val = angle_degrees * pi / 180

    # Calculate trigonometric values
    sin_val = math.sin(angle_degrees)
    cos_val = math.cos(angle_degrees)
    tan_val = math.tan(angle_degrees)

    # Return the calculated values
    print("sine = " + str(sin_val))
    print("cosine = " + str(cos_val))
    print("tangent = " + str(tan_val))
    print("radians = " + str(rad_val))


def len_conversion():
    metric_conversions_available = [(1, 'mm', 'in'),
                                    (2, 'cm', 'in'),
                                    (3, 'm', 'in'),
                                    (4, 'm', 'ft'),
                                    (5, 'km', 'yd'),
                                    (6, 'km', 'mi')
                                    ]

    standard_conversions_available = [(1, 'in', 'mm'),
                                      (2, 'in', 'cm'),
                                      (3, 'ft', 'cm'),
                                      (4, 'ft', 'm'),
                                      (5, 'yd', 'm'),
                                      (6, 'yd', 'km'),
                                      (7, 'mi', 'km')]
    print()
    print("1 for metrics to standard. 2 for standard to metrics. ")
    print()
    len_choice = int(input("Please input your choice of conversion: "))
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
            out_val = str(in_val * 25.4)
            print(str(in_val) + " in inches is " + out_val + " in mm")

        if conversion_index == 1:
            out_val = str(in_val * 2.54)
            print(str(in_val) + " in inches is " + out_val + " in cm")

        if conversion_index == 2:
            out_val = str(in_val * 30.48)
            print(str(in_val) + " in foot is " + out_val + " in cm")

        if conversion_index == 3:
            out_val = str(in_val / 0.3048)
            print(str(in_val) + " in foot is " + out_val + " in m")

        if conversion_index == 4:
            out_val = str(in_val / 1.094)
            print(str(in_val) + " in yards is " + out_val + " in m")

        if conversion_index == 5:
            out_val = str(in_val / 1094)
            print(str(in_val) + " in yards is " + out_val + " in km")

        if conversion_index == 6:
            out_val = str(in_val * 1.609)
            print(str(in_val) + " in miles is " + out_val + " in km")

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
                print("Invalid input. Only enter numbers 1-6")

        print()
        in_val = float(input("Enter input unit: "))
        print()

        if conversion_index == 0:
            out_val = str(in_val / 25.4)
            print(str(in_val) + " in mm is " + out_val + " in inches")

        elif conversion_index == 1:
            out_val = str(in_val / 2.54)
            print(str(in_val) + " in cm is " + out_val + " in inches")

        elif conversion_index == 2:
            out_val = str(in_val * 39.3701)
            print(str(in_val) + " in m is " + out_val + " in inches")

        elif conversion_index == 3:
            out_val = str(in_val * 3.281)
            print(str(in_val) + " in m is " + out_val + " in foot")

        elif conversion_index == 4:
            out_val = str(in_val * 1093.61)
            print(str(in_val) + " in km is " + out_val + " in yards")

        elif conversion_index == 5:
            out_val = str(in_val / 1.609)
            print(str(in_val) + " in km is " + out_val + " in miles")


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
            print(str(in_val) + " in US tonnes is " + out_val1 + " in km and " + out_val2 + " in tonnes")

        if conversion_index == 6:
            out_val1 = str(in_val * 1016)
            out_val2 = str(in_val * 1.016)
            print(str(in_val) + " in Imperial tonnes is " + out_val1 + " in km and " + out_val2 + " in tonnes")

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


outcomes = ["A", "S", "D", "M", "MO", "PO", "Q", "SQ", "TRI", "CON"]
trigonometric_outcomes = ["R", "I"]
inverse_trigonometric_outcomes = ["S", "C", "T"]
while True:

    print("(A)dd, (S)ubtract, "
          "(D)ivide, (M)ultiply, (MO)dulus, (PO)wer of, (SQ)uare root, (TRI)g, (CON)version, or (Q)uit ")
    print()
    while True:
        choice = input("Which calculation would you like to operate? ").upper()
        print()
        if choice in outcomes:
            break
        else:
            print("Invalid input. Only enter: A, S, D, M, MO, PO, Q. Please try again! ")
            print()
            continue

    if choice == "A":
        print("User wants to add ")
        print()

        numbers = collect_inputs()

        result = check_integer(sum(numbers))
        print("The answer is: " + str(result))
        print()
        continue

    elif choice == "S":
        print("User wants to subtract ")
        print()

        numbers = collect_inputs()
        result = numbers[0]
        for num in numbers[1:]:
            result -= num

        result = check_integer(result)
        print("The answer is: " + str(result))
        print()
        continue

    elif choice == "D":
        print("User wants to divide ")
        print()

        numbers = collect_inputs()

        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Sorry! You can't divide by 0! We're only gonna divide the prior values! ")
                print()
            else:
                result /= num
                result = check_integer(result)
                print("The answer is: " + str(result))
                print()
        continue

    elif choice == "M":
        print("User wants to multiply ")
        print()

        numbers = collect_inputs()

        result = numbers[0]
        for num in numbers[1:]:
            result *= num

        result = check_integer(result)
        print("The answer is: " + str(result))
        print()
        continue

    elif choice == "MO":
        print("User wants to use modulus ")
        print()

        numbers = collect_inputs()

        result = numbers[0]
        for num in numbers[1:]:
            result %= num

        print("The answer is: " + str(result))
        print()
        continue

    elif choice == "PO":
        print("User wants to use power of ")
        print()

        numbers = collect_inputs()

        result = numbers[0]
        for num in numbers[1:]:
            result **= num

        result = check_integer(result)
        print("The answer is: " + str(result))
        print()
        continue

    elif choice == "SQ":
        while True:
            num = input("User want to find the square root of: ")
            print()
            if num.isdigit():
                result = float(num) ** (1 / 2)
                result = check_integer(result)
                print("The answer is: " + str(result))
                print()
                break
            elif num.upper() == "Q":
                break
            else:
                print("Invalid input. Please enter a number. ")
                print()
        continue

    elif choice == "TRI":

        while True:
            trigonometric_choice = input("Would you like to use (R)egular or (I)nverse "
                                         "trigonometrical functions? ").upper()
            print()
            if trigonometric_choice in trigonometric_outcomes:
                break
            else:
                print("Sorry, you can only enter either R or I. Please try again! ")
                print()
                continue

        if trigonometric_choice == "R":
            calculate_trigonometric_values()

        elif trigonometric_choice == "I":
            while True:
                inverse_choice = input("Are you trying to convert"
                                       " from Sine, Cosine, or Tangent? ").upper()
                print()
                if inverse_choice in ("I", "S", "T"):
                    break
                else:
                    print("Invalid input. you can only enter either R or I. Please try again! ")
                    print()
                    continue

            if inverse_choice == "S":
                while True:
                    value = float(input("Input the value of the ratio: "))
                    print()
                    if -1 <= value <= 1:
                        print("the arcsin of " + str(value) + " is " + str(math.degrees(math.asin(value))) + " degrees")
                        print()
                        break
                    else:
                        print("Invalid input. Only input a number from -1 to 1 ")
                        print()

            elif inverse_choice == "C":
                while True:
                    value = float(input("Input the value of the ratio: "))
                    print()
                    if -1 < value < 1:
                        print("the arccos of " + str(value) + " is " + str(math.degrees(math.acos(value))) + " degrees")
                        print()
                        break
                    else:
                        print("Invalid input. Only input a number from -1 to 1 ")
                        print()

            elif inverse_choice == "T":
                value = float(input("Input the value of the ratio: "))
                print()
                print("the arctan of " + str(value) + " is " + str(math.degrees(math.atan(value))) + " degrees")
                print()

        continue

    if choice == "CON":
        print("User wants to use conversions. ")
        print()
        while True:
            print("1 for length conversions, 2 for mass conversions ")
            conversion_choice = int(input("Enter the conversion type you'd like to use: "))
            if conversion_choice in (1, 2):
                break
            else:
                print("Invalid input. Only enter: ")
        if conversion_choice == 1:
            len_conversion()
        if conversion_choice == 2:
            mass_conversion()

    elif choice == "Q":
        break
