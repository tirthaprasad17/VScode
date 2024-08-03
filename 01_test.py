str = "geeks for geeks"
str2 = "Code of the    Day"


def get(s):
    str = ""
    temp = ""
    for i in range(len(s)-1, 0, -1):
        if s[i].isalpha() and s[i-1] == ' ':
            temp += s[i]
    str += s[0]
    for i in range(len(temp)-1, -1, -1):
        str += temp[i]
    print(str)
 
get(str)
get(str2)