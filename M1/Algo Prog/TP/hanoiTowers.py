# departure tower
# destination tower
# third tower that is neither
towerlst = [[1,2],[3],[]]

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
    # remove the top disk/ first element
    # add to head of destination tower
    displaysMovement(dep, dest)
    print(towerlst)
    # display movement
    # display resulting Hanoi Towers
    # return new towerlst value

motion(towerlst,0,1)
