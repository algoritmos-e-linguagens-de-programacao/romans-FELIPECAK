def int_to_roman(num): 
    sub = num
    while sub != 0:
        if sub == 4:
            print("IV", end="")
            sub -= 4
        elif sub == 9:
            print("IX", end="")
            sub -= 9
        elif sub >= 40 and sub < 50:
            print("XL", end="")
            sub -= 40
        elif sub >= 90 and sub < 100:
            print("XC", end="")
            sub -= 90
        elif sub >= 400 and sub < 500:
            print("CD", end="")
            sub -= 400
        elif sub >= 900 and sub < 1000:
            print("CM", end="")
            sub -= 900
        elif sub == 1:
            print("I", end="")
            sub -= 1
        elif sub < 5:
            print("I", end="")
            sub -= 1
        elif sub < 10:
            print("V", end="")
            sub -= 5
        elif sub < 50:
            print("X", end="")
            sub -= 10
        elif sub < 100:
            print("L", end="")
            sub -= 50
        elif sub < 500:
            print("C", end="")
            sub -= 100
        elif sub < 1000:
            print("D", end="")
            sub -= 500
        elif sub >= 1000:
            print("M", end="")
            sub -= 1000
    
def roman_to_int(roman):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
}

    total = 0
    prev_value = 0

    for symbol in reversed(roman):
        value = roman_values[symbol]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
roman_numeral = "MMXVIII"

