
# finding the largest in a list 
list = [3, 4, 23, 56, 6767]

max_number = list[0]


for number in list:
    if number > max_number:
        max_number = number

print(max_number) 



# check whether a number is an even number or od


numbers = [3, 6, 5, 4, 44, 89, 68, 70, 50, 30]

def checkNumbers():
    for number in numbers:
        if number%2 == 0:
            print(f'{number}' + ' is even number')

        else:
            print(f'{number}' + ' is an odd number')

checkNumbers()


















