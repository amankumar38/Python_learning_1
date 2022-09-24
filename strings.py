#Strings : ordered, immutable, text representation

from timeit import default_timer as timer
my_string = "Hello World"
print(my_string.isupper())
print(my_string.islower())
print(my_string.upper())
print(my_string.lower())
print(my_string.capitalize())
print(my_string.swapcase())
print(my_string.count('o'))
print(my_string.index('e'))
print(my_string.replace("World", "Universe"))

Str = '               Hello world             '
print(Str)
Str = Str.strip()
print(Str)

my_str = "How are you doing"
my_str_list = my_str.split(" ")
print(my_str_list)

my_str = "How,are,you,doing"
my_str_list = my_str.split(" ")
print(my_str_list)
my_str_list = my_str.split(",")
print(my_str_list)
new_str = ' '.join(my_str_list)
print(new_str)


my_lst = ['a']*1000000
# print(my_lst)

#now to join the list to form a word

start = timer()
my_strings = ''
for i in my_lst:
    my_strings += i
stop = timer()
print(stop-start)

#above code is bad code as it creat a new string

start = timer()
my_strings = ''.join(my_lst)
# print(my_strings)
stop = timer()
print(stop-start)

#avobe code is good code it is also faster

# %, .format(), f-string
var = 'hello'
var2 = 3
var3 = 3.147895325
my_var = "%s world" % var
my_var2 = "the value of var2 is %d" % var2
my_var3 = "the value of var2 is %f" % var3
my_var3_1 =  "the value of var2 is %.3f" % var3 #to specify integar after decimal point

print(my_var)
print(my_var2)
print(my_var3)
print(my_var3_1)