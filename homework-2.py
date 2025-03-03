# code -1: sum of non prime numbers
num1 = int(input("Enter any number: "))
sum = 0
while(num1 > 0):
    digit = num1 % 10
    is_prime = True
    for i in range(2, int(digit ** 0.5) + 1):
        if digit % i == 0:
            is_prime = False
            break
    if(is_prime == False) :
        sum += digit
    num1 = num1 // 10
print(sum)

# code - 2: Perfect number
num1 = int(input("Enter a number: "))
sum = 0
for i in range(1, (num1 // 2) + 1):
    if(num1 % i == 0):
        sum += i
if(num1 == sum):
    print("Perfect")
else:
    print("Not Perfect")

# code - 3: Sum of odd numbers
num1 = input("Enter any number: ")
sum = 0
li = [int(x) for x in num1]
for i in li:
    if i % 2 == 1:
        sum +=i
print("The sum is", sum)

# code - 4: L.C.M of 2 numbers
num1, num2 = map(int, input("Enter two numbers: ").split(" "))
def lcm_of_two_numbers(num1, num2):
    if(num1 > num2):
        largest = num1
    else:
        largest = num1
    i = 1
    while(True):
        value = largest * i
        if value % num1 == 0 and value % num2 == 0:
            return value
        i +=1

lcm = lcm_of_two_numbers(num1, num2)
gcd = (num1 * num2) // lcm_of_two_numbers(num1, num2)
print("L.C.M is", lcm, "G.C.D is", gcd)



              

