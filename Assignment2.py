# Task 1
print("Check if a number is Even or Odd")
num = int(input('Enter a number: '))

if num % 2 == 0:
    print(num,'is an even number')

else:
    print(num,'is an odd number')



# Task 2
print("--------------------------------------------")
print("Sum of Integers from 1 to 50 Using a Loop")
sum = 0
for n in range(1,51):
    sum +=n
print(f'The sum of numbers from 1 to 50 is: {sum}')