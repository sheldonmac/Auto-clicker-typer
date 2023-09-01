animals = ["seal", "cat", "frog", "orangatang", "lobster", "elephant", "cow", "flying fish", "polar bear", "monkey", "red fox", "donkey", "chimp", "box jelly", "gorila", "koala", "otter", "sheep", "red panda"]
questions = ["vertibre", "fur", "feathers", "dry skin", "scales"]
ans = []
for y in animals:
    for x in questions:
        z = input("does a " + y + " have a " + x + ": ")
        if z == "y":
            ans.append(y + " has " + x)
        if z == "n":
            ans.append(y + " does not have "+ x)
        
print(ans)