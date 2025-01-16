roman_map = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def into_roman(num):
    res = ""
    while num > 0:
        for i, r in roman_map:
            while num >= i:
                res += r
                num -= i
    return res


num = int(input("Enter a number: "))
print(into_roman(num))