GST = 0.15

item = float(input("Enter item price: "))
item_GST = item * GST
total_cost = item + item_GST

print("Total cost: {}".format(total_cost))
