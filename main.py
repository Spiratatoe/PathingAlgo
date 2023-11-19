import json

#written by jack
def solve(str1, str2):
    # load file
    fileName = 'labyrinths/' + str1 + '/labyrinth_' + str2 + '.json'
    with open(fileName, 'r') as f:
        data = json.load(f)

    # data we need
    choices = data.get("tiles")
    start = data.get("start")
    end = data.get("end")

    # filter it and get list of coords where we may move
    stored = []
    for x in choices:
        # check the type first, we need to store the normal types
        typeTile = x[1].get('type')
        if typeTile == 'TileType.NORMAL':
            # get coordinates
            coords = [x[0].get('a'), x[0].get('r'), x[0].get('c')]
            stored.append(coords)

    # get coords for start and end
    startCoord = [start.get('a'), start.get('r'), start.get('c')]
    endCoord = [end.get('a'), end.get('r'), end.get('c')]

    # pathfinding algorythm using A* logic
    openCoords = []  # coordinates adjacent to start and choices
    openValues = []  # this is so we know the associated values to a choice
    closedCoords = []  # coordinates where we passed by
    closedValues = []
    current = startCoord  # current is where you are, initial pt is start
    found = False
    dist = 0
    current.append(dist)
    cost = 0
    current.append(cost)
    tot = 0
    current.append(tot)
    x = 1
    while not found:
        x = x + 1
        # find all adjacent to current space
        # to do this, calculate the 6 options and see if any in choices list
        a = current[0]
        r = current[1]
        c = current[2]
        # nearest neighbor from wikipedia
        opt1 = [a, r, c - 1]
        opt2 = [a, r, c + 1]
        opt3 = [1 - a, r - (1 - a), c - (1 - a)]
        opt4 = [1 - a, r - (1 - a), c + a]
        opt5 = [1 - a, r + a, c - (1 - a)]
        opt6 = [1 - a, r + a, c + a]
        verify = [opt1, opt2, opt3, opt4, opt5, opt6]
        for opt in verify:
            if not found:
                # first see if end is in options
                print(verify)
                print("current is, ",current)
                print(closedValues)
                if opt == endCoord:
                    print("found the end")
                    found = True  # found we may end
                if not found:
                    if opt not in closedCoords:
                        if opt in stored:
                            # store just the coords first
                            openCoords.append(opt)
                            # add the distance value
                            dist = abs(endCoord[0] - opt[0]) + abs(endCoord[1] - opt[1]) + abs(endCoord[2] - opt[2])
                            opt.append(dist)
                            # cost value
                            cost = current[4] + 1
                            opt.append(cost)
                            # total
                            tot = dist * cost
                            opt.append(tot)
                            openValues.append(opt)
        # added this because first one doesn't break out
        if not found:
            # now pick which one becomes next current
            # we take the one with the smallest dist, if dist are the same lower cost, if cost the same, first in list
            openValues.sort(reverse=True, key=lambda j: j[4])  # sort so the highest cost is the first in next sort
            # sort the openValues by tot, so we can pick the lowest total as next move
            openValues.sort(key=lambda j: j[5])

            # make first new current, remove it from open, add it the closed
            current = openValues[0]
            openValues.pop(0)
            temp = [current[0], current[1], current[2]]
            closedCoords.append(temp)
            closedValues.append(current)

    # start to backtrack
    # we want to take the option that is 1 cost less than the most recent move
    if not closedValues:
        closedValues.append(current)
        temp = [current[0], current[1], current[2]]
        closedCoords.append(temp)

    reached = False
    # get moves it takes
    temp = closedValues.pop()
    moves = temp[4]
    path = [endCoord]
    path.append(temp)

    if not closedValues:
        reached = True
    while not reached:
        temp = closedValues.pop()
        if temp[4] == moves - 1:
            path.append(temp)
            moves = temp[4]
        if moves == 1:
            reached = True

    path.append(startCoord)



    # write answer in solution folder
    fileName2 = 'solutions/' + str1 + '/labyrinth_' + str2 + '.txt'
    f = open(fileName2, "w+")
    for i in path:
        coord = "(" + str(i[0]) + ", " + str(i[1]) + ", " + str(i[2]) + ")\n"
        f.write(coord)

def solveEasy():
    for number in range(100):
        if number < 10:
            tempString = "0" + str(number)
            solve("easy", tempString)
            print(number)
        else:
            tempString = str(number)
            solve("easy", tempString)
            print(number)
def solveExtreme():
    for number in range(100):
        if number < 10:
            tempString = "0" + str(number)
            solve("extreme", tempString)
            print(number)
        else:
            tempString = str(number)
            solve("extreme", tempString)
            print(number)
def solveHard():
    for number in range(100):
        if number < 10:
            tempString = "0" + str(number)
            solve("hard", tempString)
            print(number)
        else:
            tempString = str(number)
            solve("hard", tempString)
            print(number)
def solveIntermediate():
    for number in range(100):
        if number < 10:
            tempString = "0" + str(number)
            solve("intermediate", tempString)
            print(number)
        else:
            tempString = str(number)
            solve("intermediate", tempString)
            print(number)
if __name__ == '__main__':
    #solve("easy", "00")
    #solve("easy","06")
    solveEasy()
    solveIntermediate()
    solveHard()
    # solveExtreme()
