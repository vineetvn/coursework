def left_rotate_array(arr: list, timesToRotate) -> list:
    if timesToRotate < 1:
        return arr

    while timesToRotate > 0:
        poppedEle = arr.pop(0)
        arr.append(poppedEle)
        timesToRotate -= 1

    return arr


print(left_rotate_array([1, 2, 3, 4, 5], 3))

# without using array methods


def left_rotate(arr: list, rotateTimes) -> list:
    if rotateTimes < 1:
        return arr

    while rotateTimes > 0:
        firstEle = arr[0]
        n = len(arr)
        for i in range(0, n - 1):
            arr[i] = arr[i+1]
        arr[n-1] = firstEle
        rotateTimes -= 1

    return arr


print(left_rotate([1, 2, 3, 4, 5], 3))
