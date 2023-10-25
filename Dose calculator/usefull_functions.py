import os, re


"""
Brief: Stop program until user press enter or if it is sett, value from optional argument: key. If key is setted, pressing enter don't let programs run again.
Param:
    inf_for_user: If has not None value, print that content before user has possibility to write.
    inf_wrong_key: If has not None value, print that content if user pass other value than enter, or if is setted key value.  If key is setted, pressing enter don't let programs run again.
    key: "str" value that user must write in console for keep running program.
Return:
    str: only if key is not "str" type.
    None.
"""
def waitForEnter(inf_for_user=None, inf_wrong_key=None, key=None):

    if key is not None:
        if type(key) is not str:
            return print("Error 5: key value must be \"str\" type, but is given: " + str(type(key)))

    while True:

        # Get input from user.
        if inf_for_user is None:
            user_input = input()
        else:
            user_input = input(inf_for_user)


        if key is None:
            if len(user_input) == 0:
                break
            else:
                if inf_for_user is not None:
                    print(inf_wrong_key)
                    continue
        elif key == user_input:
            break
        else:
            if inf_for_user is not None:
                print(inf_wrong_key)
            continue

"""
Brief: check if in string are dot or minus. Also check at what index is for minus.
Param: string.
Return: bool or (bool + haw many minus are in string; minus for this minus; and how many dots are in string).
"""
def isNumberWithDotOrMinus(user_input):

    minusCounter = 0
    minusIndex = None
    dotCounter = 0
    buffor = ""

    for index, char in enumerate(user_input):

        if char == "-":
            minusCounter += 1
            minusIndex = index
        elif char == ".":
            dotCounter += 1
        else:
            buffor = buffor + char

    # Check is only one minus at front of "user_input" and is only one dot.
    if minusCounter <= 1 and dotCounter <= 1 and (minusIndex == 0 or minusIndex is None):
        numeric = buffor.isnumeric()
        if numeric is True:
            return True, minusCounter, minusIndex, dotCounter
        else:
            return False
    else:
        return False

"""
Brief: Function for prepere numeric input: remove all whitespace sign and change all "," to ".".
Param: user_input: string
Return: prepered input: string
"""
def prepereNumericInput(user_input: str):

    # Change all commas to dots in "user_input".
    user_input = user_input.replace(",", ".")

    # Get rid of whitespace character from "user_input".
    whitespace_list = [" ", "\t", "\n", "\v", "\f", "\r"]
    for space in whitespace_list:
        user_input = user_input.replace(space, "")

    return user_input

"""
Brief: Function check if str type variable "data" is a number and return it as int or float type.
Param:
    data: str type (string to check)
    dtype: data type of returned value.
Return:
    str: if string is a number.
    False: if string is not a number.
"""
def isNumber(data: str):

    # Check if provided argument is str type.
    if type(data) is not str:
        exit(1)

    # Prepere data and check if argument has minus or dot.
    data = prepereNumericInput(data)
    if data.isnumeric():
        return data
    else:
        pack = isNumberWithDotOrMinus(data)

        if type(pack) is tuple:
            number = pack[0]
            with_dot = pack[3]

            if number is True and with_dot != 0:
                return data
            elif number is True and with_dot == 0:
                return data

        if type(pack) is bool and pack is True:
            return data
        else:
            return False

def is_a_hexadecimal_color(data):
    
    if type(data) is not str:
        return False
    
    if len(data) != 7:
        return False
    
    if data[0] != "#":
        return False
    
    proper_value = "[0-9 a-f A-F]"
    
    x = re.findall(proper_value, data[1:])

    if len(x) != 6:
        return False
    
    return data

def isNumberWithDot(user_input: str):

    minusCounter = 0
    minusIndex = None
    dotCounter = 0
    buffor = ""

    user_input = prepereNumericInput(user_input)

    for index, char in enumerate(user_input):

        if char == "-":
            minusCounter += 1
            minusIndex = index
        elif char == ".":
            dotCounter += 1
        else:
            buffor = buffor + char

    # Check is only one minus at front of "user_input" and is only one dot.
    if minusCounter == 0 and dotCounter <= 1 and  minusIndex is None:
        numeric = buffor.isnumeric()
        if numeric is True:
            return user_input
        else:
            return False
    else:
        return False

