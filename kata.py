def string_add(str):
    sum = 0
    if not str:
        return sum
    #str = str.replace("\n", ",")
    arr = str.split('\n')
    for i in range(0, len(arr)):
        small_arr = arr[i].split(',')
        for element in small_arr:
        	sum += int(element)
    return sum