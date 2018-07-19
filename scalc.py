import sys
def string_add(input, out=sys.stdout):
    sum = 0
    if not input:
        return sum

    sum = 0
    if not input:
        return sum
    delimiters = determine_delimiter(input)
    input = input.replace("\n", delimiters[0])

    if len(delimiters) > 1:
        for delimiter in delimiters[1:]:
            input = input.replace(delimiter, delimiters[0])

    arr = input.split(delimiters[0])

    if input[0] == '/':
        arr.pop(0)
        arr.pop(0)
    for i in range(0, len(arr)):
        if arr[i] == ']' or arr[i] == '][':
            continue
        if int(arr[i]) < 0:
            throw_negative_exception(arr)
        if int(arr[i]) > 1000:
            pass
        else:
            sum += int(arr[i])
    out.write(str(sum))
    return sum 

def throw_negative_exception(arr):
    negatives = ''
    for char in arr:
        if int(char) < 0:
            negatives += (' ' + char)
    raise ValueError("no negatives allowed:" + negatives)

def determine_delimiter(input):
    delimiter = []
    if input[0] == '/':
        delimiter.append(input[2])
    else:
        delimiter.append(',')
    
    if delimiter[0] == '[':
        delimiter = []
        this_delimiter = ''
        for char in input[3:]:
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
    



if __name__ == "__main__":
    args = sys.argv
    string_add(args[1])
