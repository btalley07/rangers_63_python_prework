#Question 1

def hello_name(user_name):
    print("Hello, " + user_name.title() + "!") 
hello_name('Blair')

def greeting(user_name):
    print('Hello {}' .format(user_name.title()))
    print(f'Hello again {user_name.title()}')
greeting('Blair')


#Question 2


odd_numbers = list(range(1,100,2))
print(odd_numbers)

def odd_numbers():
    for i in range(0,100):
        if i % 2 != 0:
            print(i)

def odd_numbers1():
    for i in range(1,101,2):
        print(i)

#Question 3

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1,2,3,4,5,0]))

def max_num_in_list(a_list):
    return max(a_list)
the_list = [45,46,200,250,24,1,0,1000]
print(max_num_in_list(the_list))

def max(a_list):
        a_list.sort()
        return a_list[-1]
        
the_list = [45,46,200,250,24,1,0,1000]
print(max(the_list))



#Question 4

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    if a_year % 100 ==0:
        return False
    if a_year % 4 == 0:
        return True
    return False
print(is_leap_year(1989))



#Question 5

a_list = 1,2,4,3,5
def is_consecutive(a_list):
    maximum = max(a_list)
    if sum(a_list) == maximum * (maximum+1)%2 :
        return True
    return False
print(is_consecutive(a_list))