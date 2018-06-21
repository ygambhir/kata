def string_add(str):
    sum = 0
    if not str:
        return sum
    str = str.replace("\n", ",")
    arr = str.split(',')
    for i in range(0, len(arr)):
    	sum += int(arr[i])
    return sum