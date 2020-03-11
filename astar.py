def Astar(state):
    global index
    frontier.append((state, mHueristics(state), [state.index(9)]))
    while frontier:
        frontier.sort(key=lambda x: x[1])
        s = frontier[0]
        # print("Top of the frontier"+str(s))
        frontier.remove(s)
        if goalState(s[0]):
            # print("Goal state "+str(s))
            index = s[2][:]
            break
        explored.append(s[0])
        determineChild(s)
