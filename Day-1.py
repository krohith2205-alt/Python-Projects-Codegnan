#Count the number of occurances ---> Suppose u have 23145676
#Repeating number is 6 get the number of occurances ---> 2
#input ---> integer, target ---> integer (count) ---> digit to find

num= int(input())
d_to_find= int(input())
count= 0
while num > 0:
    digit= num%10 #it returns the last digit
    if digit == d_to_find:
        count +=1
        num = num // 10
print(f"count of digit is {count}")
