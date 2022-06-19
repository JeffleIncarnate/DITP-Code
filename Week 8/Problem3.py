# Princliple * interst / 100

def get_interest(p, r, t):
    r = r / 100
    total = p * r * t
    return total

print(get_interest(3000, 3.5, 5))
