def shift(c, r):
    global emptyc, emptyr
    display.blit(
        tiles[state[(c, r)]],
        (emptyc * TILE_WIDTH, emptyr * TILE_HEIGHT))
    display.blit(
        tiles[EMPTY_TILE],
        (c * TILE_WIDTH, r * TILE_HEIGHT))
    tempE = state[(emptyc, emptyr)]
    state[(emptyc, emptyr)] = state[(c, r)]
    state[(c, r)] = tempE
    (emptyc, emptyr) = (c, r)
    pygame.time.delay(100)
    pygame.display.flip()



def newshift(c, r, emptyc, emptyr):
    emptyc, emptyr
    display.blit(
        tiles[state[(c, r)]],
        (emptyc * TILE_WIDTH, emptyr * TILE_HEIGHT))
    display.blit(
        tiles[EMPTY_TILE],
        (c * TILE_WIDTH, r * TILE_HEIGHT))
    tempE = state[(emptyc, emptyr)]
    state[(emptyc, emptyr)] = state[(c, r)]
    state[(c, r)] = tempE
    (emptyc, emptyr) = (c, r)
    pygame.display.flip()


def AIshift():
    initBlank = index[0]
    index.remove(initBlank)
    initBlankCol = int(initBlank % 3)
    initBlankRow = int(initBlank / 3)
    # print("Initial blank "+str(initBlank))
    while index:
        # event = pygame.event.wait()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        nextBlank = index[0]
        index.remove(nextBlank)
        # print("next position blank"+str(nextBlank))
        nextBlankrow = int(nextBlank / 3)
        nextBlankcol = int(nextBlank % 3)
        pygame.time.delay(150)
        newshift(nextBlankrow, nextBlankcol, initBlankRow, initBlankCol)
        initBlankCol = nextBlankcol
        initBlankRow = nextBlankrow
    # pygame.time.delay(1000)


# shuffle the puzzle by making some random shift moves
def shuffle():
    global emptyc, emptyr
    # keep track of last shuffling direction to avoid "undo" shuffle moves
    last_r = 0
    # shift(emptyc - 1, emptyr)
    # shift(emptyc - 1, emptyr)
    for i in range(75):
        # slow down shuffling for visual effect
        pygame.time.delay(50)
        while True:
            # pick a random direction and make a shuffling move
            # if that is possible in that direction
            r = random.randint(1, 4)
            if (last_r + r == 5):
                # don't undo the last shuffling move
                continue
            if r == 1 and (emptyc > 0):
                shift(emptyc - 1, emptyr)  # shift left
            elif r == 4 and (emptyc < COLUMNS - 1):
                shift(emptyc + 1, emptyr)  # shift right
            elif r == 2 and (emptyr > 0):
                shift(emptyc, emptyr - 1)  # shift up
            elif r == 3 and (emptyr < ROWS - 1):
                shift(emptyc, emptyr + 1)  # shift down
            else:
                # the random shuffle move didn't fit in that direction
                continue
            last_r = r
            break  # a shuffling move was made
    pygame.time.delay(1000)


def convertToArray():
    global state
    array = []
    for c in range(COLUMNS):
        for r in range(ROWS):
            # print("goalState = "+str(state[c,r][0])+str(state[c,r][1]))

            value = state[(c, r)][0] * 3 + state[(c, r)][1] + 1
            array.append(value)
    return array


def mHueristics(state):
    counter = 0
    for i in range(len(state)):
        value = state[i]
        if value != 0:
            row = int(i / 3)
            col = int(i % 3)
            expRow = int((value - 1) / 3)
            expCol = int((value - 1) % 3)
            diff = abs(row - expRow) + abs(col - expCol)
            # print(diff)
            counter += diff
    return counter


def goalState(state):
    return True if mHueristics(state) == 0 else False


def determineChild(frontierTuple):
    print("Deteminig Child")
    global frontier
    ms = []
    currentState = frontierTuple[0][:]
    currentHueristics = frontierTuple[1]
    path = frontierTuple[2][:]

    zeroIndex = currentState.index(9)
    row = int(zeroIndex / 3)
    col = int(zeroIndex % 3)
    actions = []
    if row < 2:
        actions.append("D")
    if row > 0:
        actions.append("U")
    if col < 2:
        actions.append("R")
    if col > 0:
        actions.append("L")
    print("Actions List " + str(actions))
    while actions:
        nrow, ncol = row, col
        # print("Inside Actions Loop")
        npath = path[:]
        nstate = currentState[:]
        action = actions.pop()
        if action == "D":
            nrow = row + 1
        elif action == "U":
            nrow = row - 1
        elif action == "R":
            ncol = col + 1
        elif action == "L":
            ncol = col - 1
        newIndex = nrow * 3 + ncol
        temp = nstate[zeroIndex]
        nstate[zeroIndex] = nstate[newIndex]
        nstate[newIndex] = temp
        npath.append(newIndex)
        if nstate not in explored:
            nextHueristics = mHueristics(nstate)
            frontier.append((nstate, nextHueristics, npath))
            ms.append((nstate, nextHueristics, npath))
