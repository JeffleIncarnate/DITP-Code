squares = int(input("Enter the number of squares you'd like: "))


def grainsYes():
    grains = 1
    for i in range(1, squares):
        if i == 1:
            print(i, grains)
        else:
            grains = grains * 2
            print(i, grains)

grainsYes()
