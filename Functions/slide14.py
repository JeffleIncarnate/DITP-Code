def calc_perimeter():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = length + width
    return area

print(round(calc_perimeter(), 2))