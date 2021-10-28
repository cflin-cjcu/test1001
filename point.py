x, y = input().split()
point = (int(x), int(y))
match point:
    case(x, y) if x > 0 and y > 0:
        print('first quadrant')
    case(x, y) if x < 0 and y > 0:
        print('second quadrant')
    case(x, y) if x < 0 and y < 0:
        print('third quadrant')
    case(x, y) if x > 0 and y < 0:
        print('fourth quadrant')
    case _:
        print('not in quadrant')
