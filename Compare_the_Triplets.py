def compareTriplets(a, b):
    scores =[0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            scores[0] += 1
        elif a[i] == b[i]:
            None
        else:
            scores[1] += 1
    return scores



print(compareTriplets([5,6,7],[3,6,10]))
