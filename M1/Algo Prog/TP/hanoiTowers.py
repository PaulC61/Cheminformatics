# departure tower
# destination tower
# third tower that is neither
towerlst = [[2],[3],[1]]

def thirdTower(dep, dest):
    if (dep == 0 and dest == 1) or (dep == 1 and dest==0):
        return 2
    elif (dep == 0 and dest == 2) or (dep == 2 and dest == 0):
        return 1
    else:
        return 0

def displaysMovement(dep, dest):
    return print("T" + str(dep) + " --> T" + str(dest))

def motion(towerlst, dep, dest):
    print(towerlst)
    towerlst[dest] = [towerlst[dep][0]] + towerlst[dest]
    towerlst[dep] = towerlst[dep][1:]
    displaysMovement(dep, dest)
    print(towerlst)
    return towerlst

def movementIsValid(towerlst, dep, dest):
    # returns True if and only if deb and dest belong to {0,1,2}
    # all one statement?
    return ((dep in [0, 1, 2] and dest in [0, 1, 2]) and (dep != dest) and (towerlst[dep] != []) and (towerlst[dep][0] < towerlst[dest][0] or towerlst[dest] == []))


    # dep and dest are different

    # the starting tower is not empty
    # the first disc of the starting tower is smaller 
    # than the first disc of the destination tower


print(movementIsValid(towerlst, 2, 0))

motion(towerlst,0,1)
