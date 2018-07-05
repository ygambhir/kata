def string_add(str):
    sum = 0
    if not str:
        return sum

    sum = 0
    if not str:
        return sum
    delimiter = ','
    if str[0] == '/':
        delimiter = str[2]

    if delimiter == '[':
        delimiter = ''
        for char in str[3:]:
            if char == ']':
                break
            else:
                delimiter += char 

    str = str.replace("\n", delimiter)
    arr = str.split(delimiter)
    if str[0] == '/':
        arr.pop(0)
        arr.pop(0)
    for i in range(0, len(arr)):
        if int(arr[i]) < 0:
            throw_negative_exception(arr)
        if int(arr[i]) > 1000:
            pass
        else:
            sum += int(arr[i])
    return sum 

def throw_negative_exception(arr):
    negatives = ''
    for char in arr:
        if int(char) < 0:
            negatives += (' ' + char)
    raise ValueError("no negatives allowed:" + negatives)
    