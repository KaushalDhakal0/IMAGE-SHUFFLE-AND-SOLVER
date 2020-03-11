def Astar(state):
    global index
    frontier.append((state, mHueristics(state), [state.index(9)]))
    while frontier:
        frontier.sort(key=lambda x: x[1])
        s = frontier[0]
        frontier.remove(s)
        if goalState(s[0]):
            index = s[2][:]
            break
        explored.append(s[0])
        determineChild(s)
