import math
from math import pi

print("***************************************************")
print("************WELCOME TO MY CALCULATOR************")
print("***************************************************")


def check_integer(input_result):
    if isinstance(input_result, float):
        if input_result.is_integer():
            input_result = int(input_result)
    return input_result


def number_input():
    while True:
        try:
            numinput1 = float(input("Enter the first number "))
        except ValueError:
            print("Sorry, please enter a number ")
        else:
            break
    while True:
        try:
            numinput2 = float(input("Enter the second number "))
        except ValueError:
            print("Sorry, please enter a number ")
        else:
            break
    return numinput1, numinput2


def number_input_for_one():
    while True:
        try:
            numinput = float(input("Enter the number "))
        except ValueError:
            print("Sorry, please enter a number ")
        else:
            break
    return numinput


def calculate_trigonometric_values(angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = angle_degrees * pi / 180

    # Calculate trigonometric values
    sine_value = math.sin(angle_degrees)
    cosine_value = math.cos(angle_degrees)
    tangent_value = math.tan(angle_degrees)

    # Return the calculated values
    return sine_value, cosine_value, tangent_value, angle_radians


outcomes = ["A", "S", "D", "M", "MO", "PO", "Q", "SQ", "TRI"]
trigonometric_outcomes = ["R", "I"]
inverse_trigonometric_outcomes = ["S", "C", "T"]
run = True
while run:
    print("(A)dd, (S)ubtract, "
          "(D)ivide, (M)ultiply, (MO)dulus, (PO)wer of, (SQ)uare root, (TRI)g (Q)uit ")

    while True:
        choice = input("Which calculation would you like to operate? ").upper()
        if choice in outcomes:
            break
        else:
            print("Sorry, you can only enter one of the following: A, S, D, M, MO, PO, Q. Please try again! ")
            continue

    if choice == "A":
        print("User wants to add ")

        (num1, num2) = number_input()

        result = num1 + num2
        result = check_integer(result)
        print(str(result))

    elif choice == "S":
        print("User wants to subtract ")

        (num1, num2) = number_input()

        result = num1 - num2
        result = check_integer(result)
        print(str(result))

    elif choice == "D":
        print("User wants to divide ")

        (num1, num2) = number_input()

        result = num1 / num2
        result = check_integer(result)
        print(str(result))

    elif choice == "M":
        print("User wants to multiply ")

        (num1, num2) = number_input()

        result = num1 * num2
        result = check_integer(result)
        print(str(result))

    elif choice == "MO":
        print("User wants to use modulus ")

        (num1, num2) = number_input()

        result = num1 % num2
        result = check_integer(result)
        print(str(result))

    elif choice == "PO":
        print("User wants to use power of ")

        (num1, num2) = number_input()

        result = num1 ** num2
        result = check_integer(result)
        print(str(result))

    elif choice == "SQ":
        print("User wants to find the sqr root of ")

        number = number_input_for_one()

        result = number ** (1 / 2)
        result = check_integer(result)
        print(str(result))

    elif choice == "TRI":

        while True:
            trigonometric_choice = input("Would you like to use (R)egular or (I)nverse "
                                         "trigonometrical functions? ").upper()
            if trigonometric_choice in trigonometric_outcomes:
                break
            else:
                print("Sorry, you can only enter either R or I. Please try again! ")
                continue

        if trigonometric_choice == "R":
            angle = float(input("Please input your angle (in degrees) "))
            [sin_result, cos_result, tan_result, radian_result] = calculate_trigonometric_values(angle)

            print("sine = " + str(sin_result))
            print("cosine = " + str(cos_result))
            print("tangent = " + str(tan_result))
            print("radians = " + str(radian_result))

        elif trigonometric_choice == "I":
            while True:
                inverse_choice = input("Are you trying to convert"
                                       " from Sine, Cosine, or Tangent? ").upper()
                if inverse_choice in ("I", "S", "T"):
                    break
                else:
                    print("Sorry, you can only enter either R or I. Please try again! ")
                    continue

            if inverse_choice == "S":
                while True:
                    value = float(input("Input the value of the ratio: "))
                    if -1 <= value <= 1:
                        print("the arcsin of " + str(value) + " is " + str(math.degrees(math.asin(value))) + " degrees")
                        break
                    else:
                        print("Sorry, only input a number from -1 to 1 ")

            elif inverse_choice == "C":
                while True:
                    value = float(input("Input the value of the ratio: "))
                    if -1 < value < 1:
                        print("the arccos of " + str(value) + " is " + str(math.degrees(math.acos(value))) + " degrees")
                        break
                    else:
                        print("Sorry, only input a number from -1 to 1 ")

            elif inverse_choice == "T":
                value = float(input("Input the value of the ratio: "))
                print("the arctan of " + str(value) + " is " + str(math.degrees(math.atan(value))) + " degrees")

    elif choice == "Q":
        run = False
