print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(y and (x or z) or not(y or z) or w):
                    print(x, y, z, w)