
def binarySearch(sortedList: list, item):
    low = 0
    high = len(sortedList)-1
    tryValue = 0
    while low <= high:
        print(sortedList[low:high])
        mid = (low + high) // 2
        guess = sortedList[mid]
        print(guess)
        tryValue += 1
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1
        else:
            print(tryValue)
            return mid
    return None



if __name__ == "__main__":
    l = list(range(0, 100))
    b = binarySearch(l, 9)
    print(b)