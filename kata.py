def string_add(str):
    sum = 0
    if not str:
        return sum

    sum = 0
    if not str:
        return sum
    delimiters = determine_delimiter(str)
    print(delimiters)
    str = str.replace("\n", delimiters[0])

    if len(delimiters) > 1:
        for delimiter in delimiters[1:]:
            str = str.replace(delimiter, delimiters[0])

    arr = str.split(delimiters[0])

    if str[0] == '/':
        arr.pop(0)
        arr.pop(0)
    for i in range(0, len(arr)):
        if arr[i] == ']' or arr[i] == '':
            continue
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

def determine_delimiter(str):
    delimiter = []
    if str[0] == '/':
        delimiter.append(str[2])
    else:
        delimiter.append(',')
    
    if delimiter[0] == '[':
        delimiter = []
        this_delimiter = ''
        for char in str[3:]:
            if char == '\n':
                break
            if char == ']':
                delimiter.append(this_delimiter)
                continue
            elif char == '[':
                this_delimiter = ''
            else:
                this_delimiter += char
    return delimiter
    