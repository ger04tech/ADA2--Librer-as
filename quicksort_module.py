def quicksort(arreg):
    if len(arreg) <= 1:
        return arreg
    else:
        apunt = arreg[0]
        left = [i for i in arreg[1:] if i < apunt]
        right = [j for j in arreg[1:] if j >= apunt]
        return quicksort(left) + [apunt] + quicksort(right)
