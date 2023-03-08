'''
Write a python function, create_largest_number(), which accepts a list of numbers and
returns the largest number possible by concatenating the list of numbers.
Note: Assume that all the numbers are two digit numbers.
'''
def create_largest_number(number_list):
    number_list.sort(reverse=True)
    a=[]
    for i in number_list:
        a.append(str(i))
    k=''
    for i in range(len(a)):
        k=k+a[i]
    return int(k)
number_list=[23,34,55]
largest_number=create_largest_number(number_list)
print(largest_number)