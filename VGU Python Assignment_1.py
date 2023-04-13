#!/usr/bin/env python
# coding: utf-8

# ## Question 1.	Python program to add two numbers
# 
# 

# In[ ]:


num1 = 8
num2 = 7

sum = num1 + num2

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# ## Question 2.Maximum of two numbers in Python
# 

# In[ ]:


a = 7
b = 52
maximum = max(a, b)
print(f'Maximum of {a}, {b} is {maximum}')


# ## Question 3.	Python Program for factorial of a number
# 

# In[ ]:


num = 7

factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# ## 4.	Python Program for simple interest
# 

# In[ ]:


def simpleInterset(A, Y, R):
    SI = (A*Y*R)/100
    return SI

A = int(input("Enter the amount: "))
Y = int(input("Enter the number of years: "))
R = float(input("Enter the rate of interest: "))

print("The simple interest is:", simpleInterset(A, Y, R))


# ## 5.	Python Program for compound interest
# 

# In[ ]:


p = float(input("Enter the principal amount : "))
t = float(input("Enter the number of years : "))
r = float(input("Enter the rate of interest : "))
ci =  p * (pow((1 + r / 100), t)) 

print("Compound interest : {}".format(ci))


# ## 6.	Python Program to check Armstrong Number
# 

# In[ ]:


num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


# ## 7.	Python Program for Program to find area of a circle
# 

# In[ ]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# ## 8.	Python program to print all Prime numbers in an Interval
# 

# In[ ]:


lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# ## 9.	Python program to check whether a number is Prime or not
# 

# In[ ]:


num = 11
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# ## 10.	Python Program for n-th Fibonacci number
# 

# In[ ]:


def solve(n):
   if n <= 2:
      return n - 1
   else:
      return solve(n - 1) + solve(n - 2)
n = 8
print(solve(n))


# ## 11.	Python Program for How to check if a given number is Fibonacci number?
# 

# In[ ]:


n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes!, it is Fibonacci number")
    else:
        print("No!, it's not Fibonacci number")


# ## 12.	Python Program for n\’th multiple of a number in Fibonacci Series
# 

# In[ ]:


def find(k, n):
   f1 = 0
   f2 = 1
   i =2;
   while i!=0:
      f3 = f1 + f2;
      f1 = f2;
      f2 = f3;
      if f2%k == 0:
         return n*i
      i+=1
   return
n = 5;
k = 4;
print("Position of n\'th multiple of k in""Fibonacci Series is: ", find(k,n));


# ## 13.	Program to print ASCII Value of a character
# 

# In[ ]:


c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# ## 14.	Python Program for Sum of squares of first n natural numbers
# 

# In[ ]:


def squaresum(n):
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)
 
    return sm
 
n = int(input("Enter the num: "))
print(squaresum(n))


# ## 15.	Python Program for cube sum of first n natural numbers

# In[ ]:


def sumOfCubes(n) :
    if n < 0:
        return
    sum = 0
    for i in range(n+1):
        sum += pow(i, 3)
    return sum

n = int(input('Enter n : '))
sum = sumOfCubes(n)
print(f'Sum : {sum}')

