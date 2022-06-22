holes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
scores = []

i = 0

def get_game():
    global i, scores, holes, hole, score
    while i < 9:
        print("Holes remaining: {}".format(holes))
        hole = int(input("Enter Hole Number from (1-9): "))
        if hole in holes:
            print("10")
            holes.remove(hole)
            score = int(input("Please enter your score for that hole: "))
            scores.append(score)
            i += 1
        else:
            print("Not a valid Hole.")
            i += 1
            continue

get_game();

totalscore = 0

for i in scores:
    totalscore += i

print("Your total score is: {}".format(totalscore))
