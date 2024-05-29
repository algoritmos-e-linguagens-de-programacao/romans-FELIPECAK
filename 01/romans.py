def int_to_roman(num): 
    roman = ""
    sub = num
    while sub != 0:
        if sub == 4:
            roman += "IV"
            sub -= 4
        elif sub == 9:
            roman += "IX"
            sub -= 9
        elif sub >= 40 and sub < 50:
            roman += "XL"
            sub -= 40
        elif sub >= 90 and sub < 100:
            roman += "XC"
            sub -= 90
        elif sub >= 400 and sub < 500:
            roman += "CD"
            sub -= 400
        elif sub >= 900 and sub < 1000:
            roman += "CM"
            sub -= 900
        elif sub == 1:
            roman += "I"
            sub -= 1
        elif sub < 5:
            roman += "I"
            sub -= 1
        elif sub < 10:
            roman += "V"
            sub -= 5
        elif sub < 50:
            roman += "X"
            sub -= 10
        elif sub < 100:
            roman += "L"
            sub -= 50
        elif sub < 500:
            roman += "C"
            sub -= 100
        elif sub < 1000:
            roman += "D"
            sub -= 500
        elif sub >= 1000:
            roman += "M"
            sub -= 1000
    return roman
    
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

