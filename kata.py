def string_add(str):
    sum = 0
    if not str:
        return sum

    arr = str.split('\n')
    delimiter = ','
    if str[0] == '/':
        delimiter = str[2]
        arr.pop(0)
    #str = str.replace("\n", ",")
    for i in range(0, len(arr)):
        small_arr = arr[i].split(delimiter)
        for element in small_arr:
        	sum += int(element)
    return sum