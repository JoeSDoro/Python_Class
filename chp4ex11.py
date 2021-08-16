# Program by Joe Doro
# Chapter 4, EX 11, PG 163

def main():
    number = int(input('Enter any number: '))
    factorial = 1

    while number > 0:
        
        factorial = factorial * number
        number = number -1

    print('The factorial of your number is: ', factorial)

main()
