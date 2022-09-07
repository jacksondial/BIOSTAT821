# Homework 1

def get_data(string):
    lst = list(string.split(" "))
    ints = []
    for i in lst:
        ints.append(int(i))
    return ints


str1 = "2 1 0 9 3"
print(get_data(str1))
