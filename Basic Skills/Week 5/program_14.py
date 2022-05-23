giftBalance = int(
    input("What is the value of the gift card you have gotten: "))

bookName = input("What book have you bought: ")
bookPrice = float(input("What was the cost of the book: "))

remaining = giftBalance - bookPrice

print("You have", remaining,
      "dollars remaining in the gift card. The book you bought is", bookName)
